/*document.addEventListener('DOMContentLoaded', function() {
    //função que cria as linhas em branco para o usuário inserir dados
    document.querySelector('#add-row').onclick = function() {
        var table = document.getElementsByTagName('table')[0];

        var newRow = table.insertRow(table.rows.length);

        var cel1 = newRow.insertCell(0);
        var cel2 = newRow.insertCell(1);
        var cel3 = newRow.insertCell(2);
        var cel4 = newRow.insertCell(3);
        var cel5 = newRow.insertCell(4);

        cel1.innerHTML = "linha 1";
        cel2.innerHTML = "linha 2";
        cel3.innerHTML = "linha 3";
        cel4.innerHTML = "linha 4";
        cel5.innerHTML = "<button class='delete-row'><img id='trash' src='/static/images/delete.png' width='24' height='24'></button>";
    }

    //função que deleta a linha escolhida pelo usuário
    document.querySelector('.delete-row').onclick = function($this) {
        var i = this.parentNode.parentNode.rowIndex;
        document.getElementsByTagName('table')[0].deleteRow(i);
    }

});
*/

//função que deleta a linha escolhida pelo usuário
function deleteRow(actualElement) {
    var index = actualElement.parentNode.parentNode.rowIndex;
    document.getElementsByTagName('table')[0].deleteRow(index);
}

//função que cria as linhas em branco para o usuário inserir dados
function addRow() {
    var table = document.getElementsByTagName('table')[0];

    var newRow = table.insertRow(table.rows.length);

    var cel1 = newRow.insertCell(0);
    var cel2 = newRow.insertCell(1);
    var cel3 = newRow.insertCell(2);
    var cel4 = newRow.insertCell(3);
    var cel5 = newRow.insertCell(4);
    var cel6 = newRow.insertCell(5);

    cel1.innerHTML = "linha 1";
    cel2.innerHTML = "linha 2";
    cel3.innerHTML = "linha 3";
    cel4.innerHTML = "linha 4";
    cel5.innerHTML = "linha 5";
    cel6.innerHTML = "<button class='delete-row' onclick='deleteRow(this)'><img id='trash' src='/static/images/delete.png' width='24' height='24'></button>";
}