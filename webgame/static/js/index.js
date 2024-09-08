let url = "http://127.0.0.1:8000/1"

let response = fetch(url);

alert (response)

if (response.ok) { // если HTTP-статус в диапазоне 200-299
  // получаем тело ответа (см. про этот метод ниже)
  alert (response.text());
} else {
  alert("Ошибка HTTP: " + response.status);
}