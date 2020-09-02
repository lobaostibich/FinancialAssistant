document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#add-row').onclick = function() {
        //fazer aqui a parte que vai criar a linha em branco na página add_records
        var tr = document.createElement('tr');
        var td = document.createElement('td');
        tr.innerHTML = td;

        document.querySelector('#registers').append(tr);
    }

});