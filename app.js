const cards = [...document.querySelectorAll('.card')];
const search = document.querySelector('#search');
const filters = [...document.querySelectorAll('.filter')];
const empty = document.querySelector('#empty');
let category = 'Toate';
function update() {
  const term = search.value.trim().toLocaleLowerCase('ro');
  let shown = 0;
  cards.forEach(card => {
    const visible = (category === 'Toate' || card.dataset.category === category) && card.dataset.search.includes(term);
    card.hidden = !visible;
    if (visible) shown++;
  });
  empty.hidden = shown !== 0;
}
filters.forEach(button => button.addEventListener('click', () => {
  category = button.dataset.filter;
  filters.forEach(item => item.classList.toggle('active', item === button));
  update();
}));
search.addEventListener('input', update);
