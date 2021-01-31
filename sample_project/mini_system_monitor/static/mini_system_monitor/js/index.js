/* eslint-env browser */
/* globals gridjs */

const grid = new gridjs.Grid({
  columns: ['Name', 'Value', 'Graph'],
  data: [
    ['Loading...', 'Loading...']
  ]
})

const defaultTimeToUpdate = 2000
let timeToUpdate = defaultTimeToUpdate

function getData () {
  const path = '/admin/mini_system_monitor/overview/api.json/'
  fetch(path)
    .then(response => response.json())
    .then(data => {
      updateUI(data)
    })
    .catch(console.error)

  setTimeout(getData, timeToUpdate)
}

function updateUI (data) {
  grid.updateConfig({
    data: data.map(d => [d.name, toPercent(d.value), progressbar(d.value)])
  }).forceRender()
}

function progressbar (text) {
  return gridjs.h('progress', { value: text, max: 100 }, text)
}

function toPercent (text) {
  return gridjs.h('strong', { }, text + '%')
}

function setupIntervalButtons () {
  const buttons = document.querySelectorAll('.interval')
  if (!buttons) return
  function intervalButton (event) {
    const button = event.target
    timeToUpdate = parseInt(button.dataset.value, 10) || defaultTimeToUpdate
    const disabledButton = document.querySelector('.interval:disabled')
    if (!disabledButton) return
    disabledButton.disabled = !disabledButton.disabled
    button.disabled = !button.disabled
  }
  buttons.forEach(button => {
    button.addEventListener('click', intervalButton)
  })
}

document.addEventListener('DOMContentLoaded', function (event) {
  console.log('DOM completamente carregado e analisado')
  setupIntervalButtons()

  setTimeout(getData, timeToUpdate)

  grid.render(document.getElementById('overview'))
})
