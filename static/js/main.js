var quest_level_1;
var quest_level_2;
// var answers_level_1 = new Map();
var answers_level_1_num = [];
var answers_level_2_num = [];
// var answers_level_1_val= new Array();
var quest_number = 0;
var count_questions = [0, 0, 0]
var global_level = 0;
window.onload = function () {
    if (window.location.href.indexOf('start_test') !== -1) {
        console.time('start')
        $.ajax({
            type: "GET",
            dataType: "json",
            async: true,
            url: 'get_level_1',
            success: function (data) {
                quest_level_1 = data
                global_level = 1
                count_questions[1] = data.length
                console.time('set_quest')
                set_quest(0, data)
                console.timeEnd('set_quest')
                console.time('secundomer')
                secundomer()
                console.timeEnd('secundomer')
            },
            error: function (data) {
                alert('error')
            }
        })
        console.timeEnd('start')
    }
}

// $('.ans1').on('click', 'button', function () {
//     let el = this
//     if (el.dataset.level == 1) {
//         answers_level_1.push(el.dataset.res)
//     }
// })


function get_answer(value, check) {
    if (global_level == 1) {
        answers_level_1_num.push([check, value])
        quest_number++
        if (answers_level_1_num.length >= count_questions[global_level]) {
            $.ajax({
                type: "GET",
                dataType: "json",
                async: false,
                url: 'get_level_2',
                data: {
                    answers: JSON.stringify(answers_level_1_num)
                },
                success: function (data) {
                    if (data != false) {
                        quest_level_2 = data
                        quest_number = 0
                        global_level = 2
                        count_questions[2] = data.length
                        document.getElementById('timeline').style.width = 0 + 'px'
                        set_quest(0, data)
                    } else {
                        alert('невнимательно')
                    }
                },
                error: function (data) {
                    alert('error')
                }
            })

        } else {
            // answers_level_1_num.push([check, value])
            // quest_number++
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
                    if (data != false) {
                        // quest_level_2 = data
                        // quest_number = 0
                        // count_questions[1] = data.length
                        // document.getElementById('timeline').style.width = 0 + 'px'
                        // set_quest(2, 0, data)
                    } else {
                        alert('невнимательно')
                    }
                },
                error: function (data) {
                    alert('error')
                }
            })

        } else {
            // answers_level_2_num.push([check, value])
            // quest_number++
            // set_quest(quest_number, quest_level_2)
            if (quest_level_2.length > quest_number) {
                set_quest(quest_number, quest_level_2)
            }
        }
    }
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

}

// function set_quest2(level, number, questions) {
//
// }


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


