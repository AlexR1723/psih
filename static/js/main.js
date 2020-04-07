var quest_level_1;
var answers_level_1 = new  Map();
window.onload = function () {
    if (window.location.href.indexOf('start_test') !== -1) {
        $.ajax({
            type: "GET",
            dataType: "json",
            async: true,
            url: 'get_level_1',
            success: function (data) {
                quest_level_1 = data
                set_quest(0, data)
                secundomer()
            },
            error: function (data) {
                alert('error')
            }
        })
    }
}

$('.ans1').on('click', 'button',function () {
    let el = this
    if (el.dataset.level == 1) {
        answers_level_1.push(el.dataset.res)
    }
})



function  get_answer(level,value,check) {
    if (level == 1) {
        answers_level_1.set(value,check)
        // answers_level_1.push(value)
    }
}

function set_quest(number, questions) {
    let quest = questions[number].quest;
    let answers = questions[number].answers;

    document.getElementById('id_questions').innerText = quest
    let div_ans = document.getElementById('id_answers')
    div_ans.innerHTML = ''
    let btn_first = document.createElement('button')
    btn_first.setAttribute('class', 'ans1')
    btn_first.setAttribute('onclick', 'get_answer('+1+','+answers.first.area+','+answers.first.check+')')
    btn_first.innerText = answers.first.text
    // btn_first.dataset.res = answers.first.area
    // btn_first.dataset.level = 1
    let btn_second = document.createElement('button')
    btn_second.setAttribute('class', 'ans1')
    btn_second.setAttribute('onclick', 'get_answer('+1+','+answers.second.area+','+answers.second.check+')')
    btn_second.innerText = answers.second.text
    // btn_second.dataset.res = answers.second.area
    // btn_second.dataset.level = 1
    div_ans.appendChild(btn_first)
    div_ans.appendChild(btn_second)
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


