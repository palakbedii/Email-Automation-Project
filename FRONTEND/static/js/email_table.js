async function loadEmailTable(endpoint, tableId, badgeColor, badgeText, showError=false) {

    console.log("Function called");
    console.log("Endpoint:", endpoint);
    
    const response = await fetch(endpoint);
    console.log("Response:", response);

    const data = await response.json();
    console.log("Data:", data);

    const table = document.getElementById(tableId);
    console.log("Table found:", table);

    table.innerHTML = "";

    if (data.emails.length === 0) {

        table.innerHTML = `
            <tr>
                <td colspan="6" class="text-center">
                    No emails found.
                </td>
            </tr>
        `;

        return;
    }

    data.emails.forEach(email => {

        table.innerHTML += `
            <tr>
                <td>${email.id}</td>
                <td>${email.recipient}</td>
                <td>${email.subject}</td>
                <td>${email.date}</td>
                <td>${email.time}</td>
                <td>
                    <span class="badge bg-${badgeColor}">
                        ${badgeText}
                    </span>
                </td>

                ${showError ? `<td>${email.error || "Unknown Error"}</td>` : ""}
            </tr>
        `;

    });

}


async function loadDashboardTable(endpoint, tableId, badgeColor, badgeText) {
    const response = await fetch(endpoint);
    const data = await response.json();
    const table = document.getElementById(tableId);

    table.innerHTML = "";

    data.emails.slice(0,5).forEach(email => {

        table.innerHTML += `
            <tr>
                <td>${email.id}</td>
                <td>${email.recipient}</td>
                <td>${email.subject}</td>
                <td>${email.date}</td>
                <td>${email.time}</td>
                <td>
                    <span class="badge bg-${badgeColor}">
                        ${badgeText}
                    </span>
                </td>
            </tr>
        `;

    });

    if(data.emails.length === 0){

        table.innerHTML = `
            <tr>
                <td colspan="6" class="text-center">
                    No emails found.
                </td>
            </tr>
        `;

    }

}