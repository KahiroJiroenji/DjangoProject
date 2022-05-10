var tabela;
$(document).ready(function(){
	
	/* Carregar conteúdo com Ajax */
    $('.fa-bars').click(function(){
   	   $('#aside').toggleClass('folded')	
	})
	
    carregarConteudo(location.hash)  
	window.onhashchange =  function() {
        carregarConteudo(location.hash)
        return false;
    };
    
    $(document).on('click', '[data-url]', function(e){
		if(location.hash == $(this).data('url')){
			carregarConteudo(location.hash)
		}else{
			location.hash = $(this).data('url')
		}
	    
	})
	
	$('[data-id]').click(function(e){
		if($(this).data('menu-horizontal') == 'True'){
			$('#view, #conteudo').html('')
			objeto = $(this)
		    carregarMenuHorizontal($(objeto).data('id'), $(objeto).data('sistema-id'))
		}else{
			$('#view').fadeOut()
		}
    	e.preventDefault()
	})
	/* Fim carregar conteúdo com Ajax */
	
	
	$(document).on('submit','form', function(event) {
//		event.preventDefault()
		objeto = $(this);
		/* Enviar formulário com Ajax */
		enviarFormulario(this)
		/* Fim enviar formulário com Ajax */
		
   });
	
	/* Remover registro com Ajax ao cliclar na classe excluir */
	$(document).on('click','.excluir',function(e){
        objeto = $(this);   
        excluirRegistro(objeto)
    })
	/* Fim remover registro com Ajax ao cliclar na classe excluir */
    
	$(document).on('click','[data-url-modal]', function(){
		$.get($(this).data('url-modal'), function(retorno){
		    $('#modal-conteudo .modal-body').html(retorno)
		    $('#modal-conteudo').modal('show')
		},'html')
	})
})

// function carregarMenuHorizontal(menu_id, sistema_id){
	
// 	 $.post(
//              '/DjangoProject/menu-horizontal/',
//              {
//                  'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(), 
//                  'menu_id': menu_id,
//                  'sistema_id': sistema_id,
//              },
//              function(retorno){
            	 
//                  try {
                     
//                      if(retorno.menu[0].nivel >= 4){
//                          var html = '<nav class="navbar navbar-expand-lg dark" style="border-radius: 0")>'
//                          html += ' <ul class="nav navbar-nav" id="menu-horizontal">'
//                          try{
//                              $(retorno.menu).each(function(k,v){
//                                  if(v.nivel == 4){
//                                      html += '<li class="nav-item dropdown">'
//                                      html += '<a class="nav-link dropdown-toggle" href="" data-toggle="dropdown" aria-expanded="true">'
//                                      html += '<span class="nav-text '+v.icone+'"> '+v.nome +' </span>'
//                                      html += '</a>'
//                                      html += '<div class="dropdown-menu dropdown-menu-scale text-color" role="menu">'
//                                  }
//                                  $(retorno.submenu).each(function(x,y){
//                                      if(y.nivel == 5 && y.menu_pai_id == v.id){
//                                         html += ' <a class="dropdown-item '+y.icone+'" href="'+y.url+'" data-url="'+y.url+'"> '+y.nome +' </a> '
//                                      }
//                                  })
//                                  if(v.nivel == 4){
//                                      html += '</div>'
//                                      html += '</li>'
//                                  }
//                              })
//                              html += '</ul>'
//                              html += '</nav>'
                            	 
//                              $('#view').html(html).fadeIn()
//                          }catch(e){
                             
//                          }
//                      }
//                  } catch (e) {
//                  }
//              },
//              'json'
//          )
// }

function carregarConteudo(url){
	var date = new Date();
	var minutes = 30;
	date.setTime(date.getTime() + (minutes * 60 * 1000));
	if(url.length){
		$.cookie('hash', url, { expires: date });
	}
	else if($.cookie('hash') == 'undefined' || !$.cookie('hash')){
		$.cookie('hash', $('li:eq(0)').find('[data-url]').data('url'), { expires: date })
	}
	
	
	
	$.get($.cookie('hash').replace('#',''), function(retorno){
		$('#conteudo').html(retorno)
		mascararCampo()
		tabela = $('.tabela-datatables').DataTable({
			"retrieve": true,
			"locales": 'pt-Br',
			"responsive": true,
			"order":[]
		})
		$('[data-url="'+$.cookie('hash')+'"]').parents('li').addClass('active')
	},'html')
	
//	location.hash = $.cookie('hash')
	return false;
	
}

function enviarFormulario(objeto){
	if($(objeto).find('[type="submit"]').data('ajax') == undefined){
		event.preventDefault();
		if($(objeto).attr('method').toUpperCase() == 'GET'){
			dados = $(objeto).serialize()
		}else{
			dados = new FormData(objeto)
		}
        $.ajax({ 
                data: dados, 
                type: $(objeto).attr('method'), 
                url: $(objeto).attr('action'), 
                processData: false,
                contentType: false,
                success: function(response) {
                	if($(objeto).find('input[type="submit"]').hasClass('btn-filter')){
                		$('#conteudo').html(response)
                	}
                	else if($(objeto).find('input[type="submit"]').data('redirect-auto') != undefined){
                		if($(objeto).find('input[type="submit"]').data('elemento') != undefined){
                			$($(objeto).find('input[type="submit"]').data('elemento')).html(response)		                        	 
                		}else{
                			$('#conteudo').html(response)		                        	 
                		}
                    }
                	else if(parseInt(response) === 1){
                         $('#mdl-msg-form').html('<div class="alert alert-success text-center">Dados salvos com sucesso</div>');
                         if($(objeto).attr('data-success-message') != "false"){
                        	 $('#mdl-msg-form').modal('show')
                         }
                       	 setTimeout(function(){
                       		 if($(objeto).find('input[type="submit"]').data('redirect') != undefined){
                                 /*url = $(objeto).find('input[type="submit"]').data('redirect')
	                             carregarConteudo(url)*/
                       			 location.hash = $(objeto).find('input[type="submit"]').data('redirect')
                             }else if($(objeto).find('input[type="submit"]').data('reload') != undefined || $(objeto).find('input[type="button"]').data('reload') != undefined){
								if ($(objeto).find('input[type="submit"]').data('refresh') == true || $(objeto).find('input[type="button"]').data('refresh') == true){
                            		 window.open($(objeto).find('[data-reload]').data('reload'), '_self')
                            	 }else{
                            		 elemento = $(objeto).find('input[type="submit"]').data('elemento')
                            		 $.get($(objeto).find('input[type="submit"]').data('reload'), function(retorno){
                            			 $(elemento).html(retorno)
                            		 },'html')
                            	 }
                             }
	                         $('.modal').modal('hide')
                       	 },1500)
                   	 }
                	
                     if(response['success'] && $(objeto).attr('data-success-message') != "true") {
                    	 $('#mdl-msg-form').html('<div class="alert alert-success text-center">Dados salvos com sucesso</div>');
                         $('#mdl-msg-form').modal('show')
                         
                         if($(objeto).find('[data-acao-btn]').data('acao-btn') == 'salvar'){
                        	 $(objeto).find('[data-acao-btn]').prop('disabled', true)
                         }
                         
                         try{
                        	 setTimeout(function(){
		                         if($(objeto).find('input[type="submit"]').data('redirect') != undefined){
//     		    	                 carregarConteudo($(objeto).find('input[type="submit"]').data('redirect'))
		                        	 location.hash = $(objeto).find('input[type="submit"]').data('redirect')
		                         }
		                         else if($(objeto).find('input[type="submit"]').data('reload') != undefined){
	                                 elemento = $(objeto).find('input[type="submit"]').data('elemento')
	                                 $.get($(objeto).find('input[type="submit"]').data('reload'), function(retorno){
	                                    $(elemento).html(retorno)
	                                },'html')
	                             }
		                         $('.modal').modal('hide')
	                       	 },1500)
                         }catch(e){
                        	 alert(e)
                         }
                     } 
                     if(response['error']) {
                   		 html = '<h2 class="text-center">Atenção</h2>';
                    	 $.each(response['error'],function(k,v){
                    		 html += '<p>'+v+'</p>';
                    		 //html += '<p>'+k.toUpperCase()+': '+v+'</p>';
                    	 })
                         $('#mdl-msg-form').html('<div class="alert alert-danger text-center">' + html +'</div>');
                         $('#mdl-msg-form').modal('show')
                     } 
                },
                error: function (request, status, error) {
                     $('#m-a-a').modal('show')
                     console.log(request.responseText);
                }
       });
	}
	/* Enviar formulário submetendo a página */
	else{
		$(objeto).submit()
	}
	/* Fim enviar formulário submetendo a página */
}

function excluirRegistro(objeto){
	if (confirm("Deseja remover o registro?")) {
        $.post($(objeto).data('url'), {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},function(retorno){
            if(retorno){
                $(objeto).closest('tr').remove()
                $('#mdl-msg-form').html('<div class="alert alert-success text-center">Ação concluída com sucesso</div>');
                $('#mdl-msg-form').modal('show')
                
                setTimeout(function(){
                	$('#mdl-msg-form').modal('hide')
                },1500)
            }
        },'html')
    }
}

function mascararCampo(){
	$('body .cep').mask('00000-000', {placeholder: "00000-000"});
	$('body .cpf').mask('000.000.000-00', {placeholder: "000.000.000-00", reverse: true});
	$('body .money').mask('000.000.000.000.000,00', {reverse: true});
	$('body .money2').mask("#.##0,00", {reverse: true});
	$('body .dateinput').mask("00/00/0000", {placeholder: "__/__/____"});
	$('body .datetimeinput').mask("00/00/0000 00:00:00", {placeholder: "__/__/____ 00:00:00"});
	$('body .hora').mask('00:00');
	$('body .timeinput').mask('00:00');
	$('body .hora-minuto').mask('00:00:00');
	$('body .telefone').mask('(00) 0000-0000',{placeholder: "(00) 0000-0000"});
	$('body .celular').mask('(00) 00000-0000',{placeholder: "(00) 00000-0000"});
}

function validarCPF(cpf)
{
  var numeros, digitos, soma, i, resultado, digitos_iguais;
  digitos_iguais = 1;
  if (cpf.length < 11)
        return false;
  for (i = 0; i < cpf.length - 1; i++)
        if (cpf.charAt(i) != cpf.charAt(i + 1))
              {
              digitos_iguais = 0;
              break;
              }
  if (!digitos_iguais)
        {
        numeros = cpf.substring(0,9);
        digitos = cpf.substring(9);
        soma = 0;
        for (i = 10; i > 1; i--)
              soma += numeros.charAt(10 - i) * i;
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(0))
              return false;
        numeros = cpf.substring(0,10);
        soma = 0;
        for (i = 11; i > 1; i--)
              soma += numeros.charAt(11 - i) * i;
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(1))
              return false;
        return true;
        }
  else
      return false;
}


function calcularIdade(aniversario, dataAtual) {
    var nascimento = aniversario.split('/');
    var dataNascimento = new Date(parseInt(nascimento[2], 10),
                  parseInt(nascimento[1], 10) - 1,
                  parseInt(nascimento[0], 10) + 1);
    
    var atual = dataAtual.split('/')
    var dataLimite = new Date(parseInt(atual[2], 10),
                  parseInt(atual[1], 10) - 1,
                  parseInt(atual[0], 10))
    
    
    var diferenca = dataLimite.getTime() -  dataNascimento.getTime();
    var idade = new Date(diferenca); // miliseconds from epoch
    return Math.abs(idade.getUTCFullYear() - 1970);
}