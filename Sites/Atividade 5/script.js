function calcularMedia() {
    
    const n1 = parseFloat(document.getElementById('nota1').value)
    const n2 = parseFloat(document.getElementById('nota2').value)
    const n3 = parseFloat(document.getElementById('nota3').value)

    const media = (n1 + n2 + n3 ) / 3
    
    let resultado = 'A média é: ' + media.toFixed(2) + ' - ';

    
    
    if (media >= 7) {
        resultado += 'Aprovado';
    } else if (media >= 4) {
        resultado += 'Recuperação';
    } else {
        resultado += 'Reprovado';
    }
    document.getElementById('resultado').innerText = resultado;

}