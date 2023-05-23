$(document).ready(function() {
  // Capturar o evento de envio do formulário
  $('#form-experiencia').submit(function(event) {
    event.preventDefault(); // Evitar o comportamento padrão do envio do formulário

    // Obter os dados do formulário
    var formData = {}; // Objeto vazio para armazenar os dados

    // Percorrer as labels desejadas e adicionar seus valores ao formData
    $('#form-experiencia label').each(function() {
      var labelFor = $(this).attr('for'); // Obter o atributo "for" da label
      var labelValue = $('#' + labelFor).text().trim(); // Obter o valor da div correspondente ao "for"
      formData[labelFor] = labelValue; // Adicionar ao formData usando o atributo "for" como chave
    });

    // Fazer a requisição AJAX
    $.ajax({
      url: 'experiencia/form',
      type: 'POST',
      data: formData,
      success: function(response) {
        // Processar a resposta da requisição
        console.log('Resposta:', response);
        // Realize as ações necessárias com a resposta recebida
      },
      error: function(error) {
        // Lidar com erros da requisição
        console.log('Erro:', error);
      }
    });
  });
});
