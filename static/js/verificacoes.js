// let nome = prompt("como você chama?")
//
// if (nome == null) {
//     alert("Recarregue a página")
// } else{
//
//     let confirmacao = confirm("Você se chama " + nome + "?")
//
// if (confirmacao) {
//     alert(nome +" bem vindo ao site recursos")
// } else {
//     alert("Recarregue a página")
// }
// }

function limpaInputsLogin() {
    const inputCpf  = document.getElementById('input-cpf')
    const inputSenha  = document.getElementById('input-email')

    inputCpf.value = ''
    inputSenha.value = ''
}

document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')
    const formCadastro = document.getElementById('form-cadastro')

    formLogin.addEventListener("submit", function (event) {
        //pegar os dois inputs do formulario
        const inputCpf = document.getElementById('input-cpf')
        const inputSenha = document.getElementById('input-senha')

        let temErro = false

        //verificar se os input's estão vazios
        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

    })

    formCadastro.addEventListener("submit", function (event) {
        //pegar os input's do cadastro
        const inputNome = document.getElementById('input-nome')
        const inputData = document.getElementById('input-data')
        const inputEmail = document.getElementById('input-email')
        const inputCpf1 = document.getElementById('input-cpf1')
        const inputSenha1 = document.getElementById('input-senha1')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        let temErro = false

        //verificar se os input's estão vazios
        if (inputCpf1.value === '') {
            inputCpf1.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf1.classList.remove('is-invalid')
        }

        if (inputSenha1.value === '') {
            inputSenha1.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha1.classList.remove('is-invalid')
        }
        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }
        if (inputData.value == '') {
            inputData.classList.add('is-invalid')
            temErro = true
        } else {
            inputData.classList.remove('is-invalid')
        }
        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }
        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }
        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }


    })

})