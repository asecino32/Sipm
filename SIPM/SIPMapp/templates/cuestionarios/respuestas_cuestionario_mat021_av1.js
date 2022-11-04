function resultado() {
    var p1, p2, p3, p4, p5, nota;

    // 1a pregunta
    if (document.getElementById('p12').checked==true) {p1=20}
    else {p1=0}
    // 2a pregunta
    if (document.getElementById('p15').checked==true) {p2=20}
    else {p2=0}
    // 3a pregunta
    if (document.getElementById('p21').checked==true) {p3=20}
    else {p3=0}
    // 4a pregunta
    if (document.getElementById('p24').checked==true) {p4=20}
    else {p4=0}
    // 5a pregunta
    if (document.getElementById('p30').checked==true) {p5=20}
    else {p5=0}
   
    nota=p1+p2+p3+p4+p5;
    alert("Calificación: " + nota,);
    window.location = 'cuestionario_mat021_av1.html'
    alert("Serás redirigido a la retroalimentación de los ejercicios")
}
