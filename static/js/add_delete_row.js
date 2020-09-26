//função que deleta a linha escolhida pelo usuário
function deleteRow(actualElement) {
    var index = actualElement.parentNode.parentNode.rowIndex;
    document.getElementsByTagName('table')[0].deleteRow(index);
}

//função que cria as linhas em branco para o usuário inserir dados
function addRow() {
    var table = document.getElementsByTagName('table')[0];

    var newRow = table.insertRow(table.rows.length);

    var cel1 = newRow.insertCell(0).style.display="none";
    var cel2 = newRow.insertCell(1);
    var cel3 = newRow.insertCell(2);
    var cel4 = newRow.insertCell(3);
    var cel5 = newRow.insertCell(4);
    var cel6 = newRow.insertCell(5);

    cel1.innerHTML = "{{form.id}}";
    cel2.innerHTML = "{{form.name}}";
    cel3.innerHTML = "{{form.category}}";
    cel4.innerHTML = "{{form.fixed}}";
    cel5.innerHTML = "{{form.value}}";
    cel6.innerHTML = "{{form.DELETE}}";
}