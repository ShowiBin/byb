$('#textarea').hide()
$('#headText').hide()
$('#textaeraToggle').click(function () {
	$('#textarea').toggle(500)
	$('#headText').toggle(500)
})

$('#menu').click(function (){
	$('#links').toggle(500)
})



function  get_blogs_data(){
			url = '/server?dataName="events"'
			$.post(url).done(set_data)
}

function set_data(obj){
	b_data = eval(obj)
	for(i in b_data){
		var cont = '<tr>\n' +
					'<td style="width: 100%;color: coral;\n"><h3>'+b_data[i][1]+':</h3><br>'+b_data[i][2]+'</td>\n' +
			'</tr>'
		$('#firstBlog').after(cont)

	}
	// $('#firstBlog').after("lalala")
	// 		return eval(obj)
}

get_blogs_data()

// locStr = (location.href)
// paras = locStr.split('?')[1]
// if (paras){
// 	nickname = paras.split('=')[1]
// 	nickname = nickname.replace('%22','').replace('%22','')
//
// 	console.log(nickname)
// 	//hide login btn
// 	$('#loginIcon').attr('href','/userPage')
// 	$('#loginIcon').text(nickname)
// 	$('#blogs_submit_btn').attr('disabled',false)
// 	$('#headText').text(nickname)
// 	//
// 	// userLink = `
// 	// 				<li><a href="/userPage" id="userHead">`+nickname+`</a></li>
// 	// `
// 	// $('#sb').after(userLink)
// 	// $('#loginIcon').hide()
//
// }


//submit blogs
$('#blogs_submit_btn').click(function () {
	console.log('clicked')
	title = $('#headText').val()
	console.log(title)
	con = $('#text').val()
	console.log(con)
	url = '/submit_events?title="'+title+'"&con="'+con+'"'
	$.post(url).done(function (res) {

		if(res == '1'){
			links = '/sorry'
			alert('Submit success')
			// console.log(content)
			$(location).prop('href','/events')

		}
		else {
			alert('Submit failed')
		}
	})
})
