/* eslint-env browser */
/* globals gridjs */

const grid = new gridjs.Grid({
  columns: ['Name', 'Value', 'Graph'],
  data: [
    ['Loading...', 'Loading...']
  ]
})

const defaultTimeToUpdate = 2000

function getData () {
  const path = '/admin/mini-system-monitor/overview/api.json/'
  fetch(path)
    .then(response => response.json())
    .then(data => {
      updateUI(data)
    })
    .catch(console.error)
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

document.addEventListener('DOMContentLoaded', function (event) {
  console.log('DOM completamente carregado e analisado')

  const urlParams = new URLSearchParams(window.location.search)
  const timeToUpdate = urlParams.get('timeToUpdate') || defaultTimeToUpdate

  setInterval(getData, timeToUpdate)
  getData()
  grid.render(document.getElementById('overview'))
})
