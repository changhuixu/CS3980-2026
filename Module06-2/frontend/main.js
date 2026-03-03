function renderTodos(data) {
  const todoDiv = document.getElementById('todos');
  todoDiv.innerHTML = '';
  data.forEach((x) => {
    todoDiv.innerHTML += `
    <div id="todo-${x.id}" class="todo-box">
        <div class="fw-bold fs-4">${x.title}</div>
        <pre class="text-secondary ps-3">${x.desc}</pre>
    </div>
    `;
  });
}

function getAllTodos() {
  const xhr = new XMLHttpRequest();
  xhr.onload = () => {
    if (xhr.status == 200) {
      data = JSON.parse(xhr.response) || [];
      console.log(data);
      renderTodos(data);
    }
  };

  xhr.open('GET', 'http://127.0.0.1:8000/todos', true);
  xhr.send();
}

(() => {
  getAllTodos();
})();
