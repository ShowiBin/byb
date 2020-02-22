
function getToBlogs(){
	try{
		if(nickname){
			hr = '/blogs?nickname="'+nickname+'"'
		}
		else {
			hr = '/login'
		}
	}
	catch (e) {
		hr = '/login'
	}

	}


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
					'<td><a href="'+b_data[i].links+'" class="link">'+b_data[i].content+'</a></td>\n' +
			'</tr>'
		$('#firstBlog').after(cont)

	}
	// $('#firstBlog').after("lalala")
	// 		return eval(obj)
}


function get_app_data() {
	$.post('/server?dataName="app"').done(function (obj) {
		var data = eval(obj)
		console.log(data)
		for(i in data){
			if(i > 18){
				break
			}
			app = data[i]

			text = '<td><a  class="showAPP" href="'+app['href']+'">\n' +
				'                                    <img class="appImg" src="'+app['img']+'"\n' +
				'                                         alt="'+app['name']+'">\n' +
				'                                </a><br><p class="desOnimg">'+app['name']+'</p></td>'
			// if(i>=0&&i<5){
			// 	$('#row1').append(text)
			// }
			// else if (i>=5&&i<10){
			// 	$('')
			// }
			console.log('#row'+Math.floor(((i/5)+1).toString()))
			console.log(i)
			$('#row'+Math.floor(((i/5)+1).toString())).after(text)
		}
	})
}


get_app_data()

//main
get_blogs_data()



locStr = (location.href)
paras = locStr.split('?')[1]
if (paras){
	nickname = paras.split('=')[1]
	nickname = nickname.replace('%22','').replace('%22','')

	console.log(nickname)
	//hide login btn
	$('#loginIcon').attr('href','/userPage')
	$('#blogs_href').attr('href','/blogs')
	$('#loginIcon').text(nickname)
	//
	// userLink = `
	// 				<li><a href="/userPage" id="userHead">`+nickname+`</a></li>
	// `
	// $('#sb').after(userLink)
	// $('#loginIcon').hide()


}
