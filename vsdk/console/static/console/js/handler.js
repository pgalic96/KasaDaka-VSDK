$(document).ready(function () {
    console.log("BLALFDAS");
        $("a .nav-link").on("click", function() {
        console.log('CLICK');
        $(".navbar-nav").find(".active").removeClass("active");
        $(this).parent().addClass("active");
    });
});

function refresh() {
    location.reload();
}




function saveOngoing() {
    const table = document.getElementById('newOrders');
    let ordersToUpdate = {orders: []};
    for (let i = 1, row; row = table.rows[i]; i++) {
        const selectedDriver = row.cells[6].getElementsByTagName('select')[0].selectedOptions[0].value;
        if (selectedDriver !== '') {
            const order = {order_id: row.cells[0].innerText, driver_id: selectedDriver};
            ordersToUpdate.orders.push(order);
        }
    }
    if (ordersToUpdate.orders.length > 0) {
        $.ajax({
            url: "/console/orders/saveOngoing",
            data: JSON.stringify(ordersToUpdate),
            method: 'POST',
            contentType: 'application/json',
            success: function(){
                location.reload();
            }
        });
    }

}

function saveFinished() {
    const table = document.getElementById('ongoingOrders');
    let ordersToUpdate = {orders: []};
    for (let i = 1, row; row = table.rows[i]; i++) {
        console.log(row.cells[7].getElementsByTagName('input')[0]);
        if (row.cells[7].getElementsByTagName('input')[0].checked === true) {
            console.log('CHECKED');
            ordersToUpdate.orders.push(row.cells[0].innerText);
        }
    }

    if (ordersToUpdate.orders.length > 0) {
        $.ajax({
            url: "/console/orders/saveFinished",
            data: JSON.stringify(ordersToUpdate),
            method: 'POST',
            contentType: 'application/json',
            success: function(){
                location.reload();
            }
        });
    }
}

function deleteDriver(driverId) {
    $.ajax({
        url: "/console/drivers/delete/" + driverId,
        method: 'DELETE',
        success: function(){
            location.reload();
        }
    });
}