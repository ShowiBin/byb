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
			url = '/server?dataName="homeBlogData"'
			$.post(url).done(set_data)
}

function set_data(obj){
	b_data = eval(obj)
	for(i in b_data){
		var cont = '<tr>\n' +
					'<td><a href="'+b_data[i].links+'" class="link"><h4>'+b_data[i].content+'</h4></a><br>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci amet enim iure natus quos suscipit totam ull</td>\n' +
			'</tr>'
		$('#firstBlog').after(cont)

	}
	// $('#firstBlog').after("lalala")
	// 		return eval(obj)
}

get_blogs_data()

locStr = (location.href)
paras = locStr.split('?')[1]
if (paras){
	nickname = paras.split('=')[1]
	nickname = nickname.replace('%22','').replace('%22','')

	console.log(nickname)
	//hide login btn
	$('#loginIcon').attr('href','/userPage')
	$('#loginIcon').text(nickname)
	//
	// userLink = `
	// 				<li><a href="/userPage" id="userHead">`+nickname+`</a></li>
	// `
	// $('#sb').after(userLink)
	// $('#loginIcon').hide()

}


//submit blogs
$('#blogs_submit_btn').click(function () {
	console.log('clicked')
	title = $('#headText').val()
	con = $('#text').val()
	console.log(con)
	url = '/submit_blogs?title="'+title+'"&con="'+con+'"'
	$.post(url).done(function (res) {
		console.log('aquared')

		if(res == '1'){
			links = '/sorry'
			alert('Submit success')
			// console.log(content)
			var cont = '<tr>\n' +
					'<td><a href="'+links+'" class="link"><h4>'+title+'</h4></a><br>con</td>\n' +con
			'</tr>'
			$('#firstBlog').after(cont)
			// get_blogs_data()
		}
		else {
			alert('Submit failed')
		}
	})
})
