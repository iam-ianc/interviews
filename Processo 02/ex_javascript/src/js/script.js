const _body = 'body';
const _selected = 'selecionada';

const _questions = 'alternativas';
const _question = 'alternativa';

const _button = '.bt';

const _hideFeedback = 'feedbacksNone';
const _pass = '#feedbackPositivo';
const _fail = '#feedbackNegativo';

$(function() {
  const arrQuestion = $(`.${_question}`);

  selectQuestion(arrQuestion)
  checkAnswer();
});

function selectQuestion(arrEl) {
  const arr = $(arrEl);
  arr.on('click', function() {
    const check = $(this);
    const question = check.closest(`.${_question}`);

    if(question.hasClass(_selected)) {
      clearQuestions();
      hideButton();
    } else {
      clearQuestions();
      question.addClass(_selected);
      showButton();
    }
  })
}

function checkAnswer() {
  $(_button).on('click', async function() {
    try {
      const res = await getData();
      const answer = res[0][0].gabarito[0].resposta;

      const { idEl } = hasAnswer(answer);

      const userSelected = $(`.${_selected}`).find('input').attr('id');

      if (userSelected == idEl){
        showFeedback(true);
        $(_body).addClass('finish');
      } else {
        showFeedback(false);
      }
    } catch(err) {
      alert('Open with Live Server VSCode!');
    }

    const finish = $(_body).hasClass('finish');

    if(finish) {
      end();
    }
  });
}

function hasAnswer(answerData) {
  const input = $(`.${_question}`).find(`input#${answerData}`)
  const idInput = input.attr('id');

  if(!!idInput) {
    return { el: input, idEl: idInput };
  } else {
    throw 'Não achamos resposta neste documento com base no gabarito.';
  }
}

function showFeedback(feedback) {
  if(feedback) {
    if(!$(_fail).hasClass(_hideFeedback)) {
      $(_fail).addClass(_hideFeedback);
    }
    $(_pass).removeClass(_hideFeedback);
  } else {
    $(_fail).removeClass(_hideFeedback);
  }
}

function showButton() {
  $(_button).show();
}

function hideButton(){
  $(_button).hide();
}

function clearQuestions() {
  $(`.${_questions}`).find(`.${_question}`).removeClass(_selected);
}

function end() {
  $(_button).attr('value', 'Acabou');
  $(_button).attr('disabled', true);
  $(_button).css({'background-color': 'transparent', 'color': '#000'});
  $(`.${_questions}`).remove();
}

function getData() {
  return new Promise((resolve, reject) => {
    fetch('./data/exercicio.js', {mode: 'no-cors'})
      .then(res => res.json())
      .then(resolve)
      .catch(reject);
  })
}
