from pathlib import Path

BASE_DIR = Path(__file__).parent
REPORTS_FOLDER = BASE_DIR / "Reports"
ARCHIVE_FOLDER = BASE_DIR / "Archive"

def get_report_files_by_addition_order():
    """
    Returns files in the Reports folder ordered by the time they
    were ADDED to the folder (creation time), NOT by filename.

    This is deliberate: filenames like '7th_Report.pdf',
    '8th_Report.pdf' do not reliably indicate sequence -- the
    user may drop files in any naming pattern. What matters is
    the order files were physically placed into the folder.

    On Windows, st_ctime reflects creation time. On Linux/Mac,
    st_ctime reflects last metadata change, so we fall back to
    st_mtime there for a more meaningful "added" timestamp -- but
    we prefer the earliest of (ctime, mtime) so a file that was
    created and never modified still sorts correctly.
    """

    if not REPORTS_FOLDER.exists():
        return []

    files = [f for f in REPORTS_FOLDER.iterdir() if f.is_file()]

    def added_time(f):
        stat = f.stat()
        # Use ctime as primary signal (creation time on Windows),
        # mtime as a secondary tiebreaker/fallback.
        return (stat.st_ctime, stat.st_mtime)

    return sorted(files, key=added_time)


def get_automatic_attachment():
    """
    Returns the earliest-added file in Reports folder --
    used when the user did not manually pick a starting file.
    """

    files = get_report_files_by_addition_order()

    if files:
        return files[0]

    return None


def get_next_attachment(current_filename):
    """
    Given the filename that was just sent, returns the NEXT file
    in the order-of-addition sequence -- i.e. whichever file was
    added to the Reports folder immediately after this one.

    Example: user manually picks '8th_Report.pdf' as the first
    attachment. Whatever file was placed into the folder right
    after '8th_Report.pdf' (regardless of its name/number) is
    returned here as the next one to send.
    """

    files = get_report_files_by_addition_order()

    for index, file in enumerate(files):

        if file.name == current_filename:

            if index + 1 < len(files):
                return files[index + 1]

            return None

    # current_filename not found (e.g. already archived/moved) --
    # nothing we can reliably determine as "next".
    return None


def archive_file(attachment_path):

    ARCHIVE_FOLDER.mkdir(exist_ok=True)
    archive_path = ARCHIVE_FOLDER / attachment_path.name
    attachment_path.rename(archive_path)


def resolve_next_attachment(current_attachment_filename):
    """
    Central place that decides what the NEXT attachment should be
    for a recurring email, given the filename that was just sent.

    - If we know the current filename, we look for the file added
      right after it (manual-first -> automatic-next chain).
    - If there's no current filename (pure automatic mode with no
      prior attachment), fall back to the earliest-added file.
    """

    if current_attachment_filename:

        next_file = get_next_attachment(current_attachment_filename)

        if next_file is not None:
            return next_file

        # No file after the current one was found in the folder
        # (it may have been archived already, or nothing new was
        # added yet) -- no next attachment available.
        return None

    return get_automatic_attachment()

