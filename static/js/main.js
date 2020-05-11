var quest_level_1;
var quest_level_2;
var quest_level_3;
// var answers_level_1 = new Map();
var answers_level_1_num = [];
var answers_level_2_num = [];
var answers_level_3_num = [];
// var answers_level_1_val= new Array();
var quest_number = 0;
var count_questions = [0, 0, 0]
var global_level = 0;
window.onload = function () {
    if (window.location.href.indexOf('start_test') !== -1) {
        // console.time('start')
        $.ajax({
            type: "GET",
            dataType: "json",
            async: true,
            url: 'get_level_1',
            success: function (data) {
                quest_level_1 = data
                // global_level = 1
                // document.getElementById('level_number').innerText='Часть '+global_level
                // count_questions[1] = data.length
                // console.time('set_quest')
                next_level(1, data)

                // console.timeEnd('set_quest')
                // console.time('secundomer')
                secundomer()
                document.getElementById('div_block_timer').style = 'position: relative;display:flex'
                // console.timeEnd('secundomer')
            },
            error: function (data) {
                alert('error')
            }
        })
        // console.timeEnd('start')
    }
    if (document.getElementById('pagename')) {
        let body = document.getElementsByTagName('body')[0]
        body.style.height = 100 + 'vh'
        // let body_height=body.getBoundingClientRect().height
        let el = document.getElementById('pagename').value
        if (el == 'Main') {

            // let mel_pos=mel.getBoundingClientRect()
            // mel.style.bottom=body_height-mel_pos.height-mel_pos.y
            // mel.style.display='block'
            // mel.style.position='absolute'
            // mel.style.bottom=5+'%'
            // mel.style.left=5+'%'
            let mel = document.getElementById('mel')
            let baba = document.getElementById('baba')
            let obl = document.getElementById('oblako')
            if (window.innerWidth > 768) {
                // let mel = document.getElementById('mel')
                mel.style = 'display:block; position:absolute; left:5%; bottom:5%; width:20%'
                // let baba = document.getElementById('baba')
                baba.style = 'display:block; position:absolute; right:10%; bottom:0px; width:27%'
                // let obl = document.getElementById('oblako')
                let baba_height = baba.getBoundingClientRect().height + 'px'
                let baba_width = window.innerWidth * 0.15 - baba.getBoundingClientRect().height * 0.3 + 'px'
                obl.style = 'display:block; position:absolute; right:' + baba_width + '; bottom:' + baba_height + '; width:10%'
            }
            // else {
            // let baba = document.getElementById('baba')
            // baba.style = 'display:block; position:absolute; right:10%; bottom:0px; width:35%'
            // let obl = document.getElementById('oblako')
            // let baba_height = baba.getBoundingClientRect().height + 'px'
            // let baba_width = window.innerWidth * 0.15 - baba.getBoundingClientRect().height * 0.3 + 'px'
            // obl.style = 'display:block; position:absolute; right:' + baba_width + '; bottom:' + baba_height + '; width:15%'
            // }
            // let babh=baba.getBoundingClientRect()
            // if (document.getElementById('start_test').getBoundingClientRect().bottom > babh.x+babh.height/2.5) {
            //     body.style.height = window.innerHeight+babh.height*0.4 + 'px'
            //     let sd=window.innerHeight-body.getBoundingClientRect().height
            //     baba.style = 'display:block; position:absolute; right:10%; bottom:'+sd+'px; width:35%'
            //     let baba_height = baba.getBoundingClientRect().height+sd + 'px'
            //     let baba_width = window.innerWidth * 0.15 - baba.getBoundingClientRect().height * 0.3 + 'px'
            //     obl.style = 'display:block; position:absolute; right:' + baba_width + '; bottom:' + baba_height + '; width:15%'
            // }
            // document.getElementById('start_test').innerHTML=window.innerWidth+'  '+window.innerHeight
        }
    }

}

// $('.ans1').on('click', 'button', function () {
//     let el = this
//     if (el.dataset.level == 1) {
//         answers_level_1.push(el.dataset.res)
//     }
// })

async function next_level(level, data) {
    global_level = level
    document.getElementById('level_number').innerText = 'Часть ' + global_level
    count_questions[level] = data.length
    quest_number = 0
    document.getElementById('timeline').style.width = 0 + 'px'
    document.getElementById('timeline').style.height = 0 + 'px'
    set_quest(0, data)
}

function get_answer(value, check) {
    if (global_level == 1) {
        answers_level_1_num.push([check, value])
        quest_number++
        if (answers_level_1_num.length >= count_questions[global_level]) {
            $.ajax({
                type: "GET",
                dataType: "json",
                async: true,
                url: 'get_level_2',
                data: {
                    answers: JSON.stringify(answers_level_1_num)
                },
                success: function (data) {
                    if (data != false) {
                        quest_level_2 = data
                        next_level(2, data)
                    } else {
                        show_result('К сожалению Вы проходили тест не внимательно. Отдохните и попробуйте повторить попытку через 7 минут', true)
                        // alert('невнимательно')
                    }
                },
                error: function (data) {
                    alert('error')
                }
            })
        } else {
            if (quest_level_1.length > quest_number) {
                set_quest(quest_number, quest_level_1)
            }
        }
    }
    if (global_level == 2) {
        answers_level_2_num.push([check, value])
        quest_number++
        if (answers_level_2_num.length >= count_questions[global_level]) {
            $.ajax({
                type: "GET",
                dataType: "json",
                async: true,
                url: 'get_level_3',
                data: {
                    answers: JSON.stringify(answers_level_2_num)
                },
                success: function (data) {
                    if (data[0] == true) {
                        show_result(data[1])
                    } else {
                        quest_level_3 = data
                        next_level(3, data)
                    }
                },
                error: function (data) {
                    alert('error')
                }
            })

        } else {
            if (quest_level_2.length > quest_number) {
                set_quest(quest_number, quest_level_2)
            }
        }
    }
    if (global_level == 3) {
        answers_level_3_num.push([check, value])
        quest_number++
        if (answers_level_3_num.length >= count_questions[global_level]) {
            $.ajax({
                type: "GET",
                dataType: "json",
                async: true,
                url: 'get_result',
                data: {
                    answers: JSON.stringify(answers_level_3_num)
                },
                success: function (data) {
                    if (data) {
                        show_result(data)

                    } else {
                        // quest_level_3 = data
                        // next_level(3,data)
                    }
                },
                error: function (data) {
                    alert('error')
                }
            })
        } else {
            if (quest_level_3.length > quest_number) {
                set_quest(quest_number, quest_level_3)
            }
        }
    }
}

function show_result(text, is_fail = false) {
    stop_timer = true
    document.getElementById('div_block_timer').remove()
    document.getElementById('div_block_quest').remove()


    if (is_fail) {
        document.getElementById('id_result').innerText = text
        document.getElementById('save_result').style.display = 'none'
        document.getElementById('label_result').innerText = 'Тест не пройден :('
    } else {
        // if (text.length>1){
        //
        // }
        // else {
        //
        // }
        document.getElementById('id_result').innerText = text[0]
        document.getElementById('save_result').dataset.conc = text[1]
        document.getElementById('save_result').dataset.time = min + '.' + sec
        document.getElementById('save_result').style.display = 'inline-block'
    }
    document.getElementById('div_result').style.display = 'flex'


}

function set_quest(number, questions) {
    if (global_level === 1) {
        var quest = questions[number].quest;
        var answers = questions[number].answers;
    } else {
        var quest = questions[number].text
        var area = questions[number].area_id
    }


    document.getElementById('id_questions').innerText = quest
    let div_ans = document.getElementById('id_answers')
    div_ans.innerHTML = ''
    let btn_first = document.createElement('button')
    btn_first.setAttribute('class', 'ans1')
    if (global_level === 1) {
        btn_first.setAttribute('onclick', 'get_answer(' + answers.first.area + ',' + answers.first.check + ')')
        btn_first.innerText = answers.first.text
    } else {
        btn_first.setAttribute('onclick', 'get_answer(' + 1 + ',' + area + ')')
        btn_first.innerText = 'Да'
    }


    let btn_second = document.createElement('button')
    btn_second.setAttribute('class', 'ans1')
    if (global_level === 1) {
        btn_second.setAttribute('onclick', 'get_answer(' + answers.second.area + ',' + answers.second.check + ')')
        btn_second.innerText = answers.second.text
    } else {
        btn_second.setAttribute('onclick', 'get_answer(' + 0 + ',' + area + ')')
        btn_second.innerText = 'Нет'
    }


    div_ans.appendChild(btn_first)
    div_ans.appendChild(btn_second)
    document.getElementById('quest_counter').innerText = 'Вопрос ' + (quest_number + 1) + ' из ' + count_questions[global_level]

    let timeline = document.getElementById('timeline')
    let div_timer = document.getElementById('div_timer')
    let tlw = div_timer.offsetWidth / count_questions[global_level] * (quest_number + 1)
    timeline.style.width = tlw + 'px'
    timeline.style.height = document.getElementById('div_timer').getBoundingClientRect().height + 'px'

}

var min = 0;
var sec = 0;
var stop_timer = false;

function secundomer() {
    sec++;
    if (sec === 60) {
        min++;
        sec = 0;
    }
    if (min < 10) {
        min1 = '0' + min
    } else {
        min1 = min
    }
    if (sec < 10) {
        sec1 = '0' + sec
    } else {
        sec1 = sec
    }
    document.getElementById('ptimer').innerText = min1 + ':' + sec1
    if (!stop_timer) {
        setTimeout('secundomer()', 1000)
    }
}


$('#save_result').click(function () {
    let name = document.getElementById('user_name').value
    let surename = document.getElementById('user_surname').value
    let patr = document.getElementById('user_patr').value
    let time = this.dataset.time
    let conc = this.dataset.conc
    $.ajax({
        type: "GET",
        dataType: "json",
        async: true,
        url: 'get_file_result',
        data: {
            name: name,
            surename: surename,
            patr: patr,
            time: time,
            conc: conc
        },
        success: function (data) {
            if (data[0]===true) {
                let link = document.createElement('a')
                link.setAttribute('href', data[1])
                link.setAttribute('download', '')
                link.setAttribute('style', 'display:none')
                link.click()
                document.getElementById('user_name').innerText = ''
                document.getElementById('user_surname').innerText = ''
                document.getElementById('user_patr').innerText = ''
                $('#modal_save_file').modal('hide')
            }else {
                document.getElementById('modal_title').innerText='Ошибка'
                document.getElementById('modal_text').innerText=data[1]
                $('#modal_id').modal('show')

            }
        },
        error: function (data) {
            alert('error')
        }
    })
})

