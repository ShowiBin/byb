$('#kikiChuchu').hide()
$('#baishe').hide()
$('#Ad_bro').hide()
$('#tuodan_league').hide()
$('#young').hide()


$('#v1').click(function () {
	$('#kikiChuchu').toggle(500)
})
// $('#v1').click(hideNavImg)
$('#v2').click(function () {
	$('#baishe').toggle(500)
})
$('#v3').click(function () {
	$('#Ad_bro').toggle(500)
})
$('#v4').click(function () {
	$('#tuodan_league').toggle(500)
})
$('#v5').click(function () {
	$('#young').toggle(500)
})


function hideNavImg() {
    setTimeout(function(){$('#navImg').slideUp();}, 2000);
}
// setTimeout(hideNavImg,3000)
hideNavImg()