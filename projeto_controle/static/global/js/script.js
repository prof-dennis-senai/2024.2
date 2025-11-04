function validarRemocao(url, msg) {
    msg = msg || "Tem certeza que deseja remover esse item?"
    if (confirm(msg)) {
        window.location.href = url
    }
}