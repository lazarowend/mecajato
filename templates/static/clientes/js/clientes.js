function add_carro(){
    container = document.getElementById("form-carro")
    html = "<div class='row mt-2' id='form_carro'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa'> </div> <div class='col-md'><input type='number' placeholder='Ano' class='form-control' name='ano'> </div></div>"
    container.innerHTML += html
}

function exibir_form(tipo) {
    add = document.getElementById("adicionar-cliente")
    att = document.getElementById("atualizar_cliente")
    if (tipo == '1') {
        add.style.display = "block";
        att.style.display = "none";
    }else if (tipo == '2') {
        add.style.display = "none";
        att.style.display = "block";
    }
}


function dados_cliente() {
    cliente = document.getElementById("select_cliente")
    id_cliente = cliente.value
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    
    if (id_cliente == ''){
        form_att = document.getElementById("form_att_cliente").style.display = "none";
        return;
    }

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function (response){
        return response.json()
    }).then(function(data){
        form_att = document.getElementById("form_att_cliente").style.display = "block";
        div_carros = document.getElementById("carros")

        id_hidden = document.getElementById("id")
        id_hidden.value = data['id_cliente']

        nome = document.getElementById("nome")
        nome.value = data['cliente']["nome"]

        sobrenome = document.getElementById("sobrenome")
        sobrenome.value = data['cliente']["sobrenome"]

        email = document.getElementById("email")
        email.value = data['cliente']["email"]

        cpf = document.getElementById("cpf")
        cpf.value = data['cliente']["cpf"]

        div_carros.innerHTML = ""
        for(i=0; i<data['carros'].length; i++){
            div_carros.innerHTML += "\<form action='/clientes/update_carro/" + data['carros'][i]['id'] +"' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' name='carro' type='text' value='" + data['carros'][i]['fields']['carro'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='placa' type='text' value='" + data['carros'][i]['fields']['placa'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='ano' value='" + data['carros'][i]['fields']['ano'] + "' >\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn btn-md btn-success' type='submit'>\
                            <a href='/clientes/excluir_carro/"+ data['carros'][i]['id'] +"' class='btn btn-md btn-danger'>EXCLUIR</a>\
                        </div>\
                    </form>\
                </div><br>"
        }
        
    })
}


function update_cliente(){
    nome = document.getElementById("nome").value
    sobrenome = document.getElementById("sobrenome").value
    email = document.getElementById("email").value
    cpf = document.getElementById("cpf").value
    id = document.getElementById("id").value

    fetch('/clientes/update_cliente/' + id, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            'nome': nome,
            'sobrenome': sobrenome,
            'email': email,
            'cpf': cpf,
        })
    }).then(function(result){
        return result.json()
    }).then(function(data){
        message = document.getElementById("message")
        if (data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            message.innerHTML = "\
                <div class='alert alert-success alert-dismissible fade show' role='alert'>\
                    <strong>Sucesso!</strong> Dadoss atualizados!!!\
                    <button type='button' class='close' data-dismiss='alert' aria-label='Close'>\
                    <span aria-hidden='true'>&times;</span>\
                    </button>\
                </div>\
            "
            console.log('ok')
        }else{
            message.innerHTML = "\
            <div class='alert alert-danger alert-dismissible fade show' role='alert'>\
                <strong>Erro!</strong> Os dados não foram atualizados!!!\
                <button type='button' class='close' data-dismiss='alert' aria-label='Close'>\
                <span aria-hidden='true'>&times;</span>\
                </button>\
            </div>\
        "
        }

    })
}

function del_carro(){
    container = document.getElementById("form_carro")
    container.remove();
}