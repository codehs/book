$(function(){
  $(".mkdown-text").each(function(idx){

      var text = $(this).text();
      $(this).html(marked(text));
  })
})