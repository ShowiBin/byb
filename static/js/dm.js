
getAttendenceData()//get the data of the attendence
getMoney()//get the data of the acounting

function getAttendenceData() {
    url = '/server?dataName="attendence"'
    $.post(url).done(set_attendence_data)
}
function set_attendence_data(obj){
    console.log(obj)
    data = eval(obj)
    for(attTimer in data){
        temp_row = data[attTimer]
        con = `<tr id="att_row`+attTimer+`">\n`

        for(var row_timer = 1;row_timer < temp_row.length - 2;row_timer++){
            con+=`<td>`+temp_row[row_timer]+`</td>\n`
        }
        con+=`</tr>`
        $('#first_row_data').after(con)
    }
}



function getMoney() {
    url = '/server?dataName="money"'
    $.post(url).done(set_money_data)
}
function set_money_data(obj){
    console.log(obj)
    data = eval(obj)
    moneyLen = data.length
    for(var moneyTimer = moneyLen - 1; moneyTimer >= 0;moneyTimer--){
        temp_row = data[moneyTimer]
        con = `<tr id="mony_row`+moneyTimer+`">\n`

        for(var row_timer = 0;row_timer < temp_row.length;row_timer++){
            con+=`<td>`+temp_row[row_timer]+`</td>\n`
        }
        con+=`</tr>`
        $('#first_row_data_money').before(con)
    }
}

