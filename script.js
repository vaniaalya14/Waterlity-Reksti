import 'regenerator-runtime/runtime';
import axios from 'axios';

const BASE_URL = 'https://shrouded-retreat-23800.herokuapp.com';

const getkelayakanminum = async () => {
  try {
    const responlayakminum = await axios.get(`${BASE_URL}/Kelayakan-minum`,{
      headers:{
        'Access-Control-Allow-Origin': '*',
      }
    });

    const todoItemslayakminum = responlayakminum.data;

    console.log(`GET: Here's the list of todos`, todoItemslayakminum);
    
    return todoItemslayakminum;
  } catch (errors) {
    console.error(errors);
  }
};
const createTodoElementlayakminum = dataread => {
  const todoElementlayakminum = document.createElement('li');todoElementlayakminum.appendChild(document.createTextNode(todoItemslayakminum.Kelayakan));

  return todoElementlayakminum;
};

const updateTodoListlayakminum = todoItemslayakminum => {
  const todoListlayakminum = document.querySelector('ul');
  todoListlayakminum.appendChild(document.createElement('br'))
  todoListlayakminum.appendChild(document.createElement('br'))
  todoListlayakminum.appendChild(document.createElement('br'))
  todoListlayakminum.appendChild(document.createElement('br'))
  todoListlayakminum.appendChild(document.createElement('li').appendChild(document.createTextNode("Kelayakan")))
  todoListlayakminum.appendChild(document.createElement('br'))
  todoListlayakminum.appendChild(document.createElement('br'))
  todoListlayakminum.appendChild(document.createElement('li').appendChild(document.createTextNode("Kelayakan air minum : " + todoItemslayakminum.Kelayakan)))
  if (todoItemslayakminum) {
    // todoList.appendChild(createTodoElement(todoItems));
    
  }
};

const getkelayakansanitasi = async () => {
  try {
    const responlayaksanitasi = await axios.get(`${BASE_URL}/Kelayakan-sanitasi`,{
      headers:{
        'Access-Control-Allow-Origin': '*',
      }
    });

    const todoItemslayaksanitasi = responlayaksanitasi.data;

    console.log(`GET: Here's the list of todos`, todoItemslayaksanitasi);
    
    return todoItemslayaksanitasi;
  } catch (errors) {
    console.error(errors);
  }
};
const createTodoElementlayaksanitasi = dataread => {
  const todoElementlayaksanitasi = document.createElement('li');todoElementlayaksanitasi.appendChild(document.createTextNode(todoItemslayaksanitasi.Kelayakan));

  return todoElementlayaksanitasi;
};

const updateTodoListlayaksanitasi = todoItemslayaksanitasi => {
  const todoListlayaksanitasi = document.querySelector('ul');
  todoListlayaksanitasi.appendChild(document.createElement('br'))
  todoListlayaksanitasi.appendChild(document.createElement('br'))
  todoListlayaksanitasi.appendChild(document.createElement('li').appendChild(document.createTextNode("Kelayakan air sanitasi : " + todoItemslayaksanitasi.Kelayakan)))
  if (todoItemslayaksanitasi) {
    // todoList.appendChild(createTodoElement(todoItems));
    
  }
};

const getkelayakantani = async () => {
  try {
    const responlayaktani = await axios.get(`${BASE_URL}/Kelayakan-tani`,{
      headers:{
        'Access-Control-Allow-Origin': '*',
      }
    });

    const todoItemslayaktani = responlayaktani.data;

    console.log(`GET: Here's the list of todos`, todoItemslayaktani);
    
    return todoItemslayaktani;
  } catch (errors) {
    console.error(errors);
  }
};
const createTodoElementlayaktani = dataread => {
  const todoElementlayaktani = document.createElement('li');todoElementlayaktani.appendChild(document.createTextNode(todoItemslayaktani.Kelayakan));

  return todoElementlayaktani;
};

const updateTodoListlayaktani = todoItemslayaktani => {
  const todoListlayaktani = document.querySelector('ul');
  todoListlayaktani.appendChild(document.createElement('br'))
  todoListlayaktani.appendChild(document.createElement('br'))
  todoListlayaktani.appendChild(document.createElement('li').appendChild(document.createTextNode("Kelayakan air untuk pertanian : " + todoItemslayaktani.Kelayakan)))
  if (todoItemslayaktani) {
    // todoList.appendChild(createTodoElement(todoItems));
    
  }
};

const getkelayakanikan = async () => {
  try {
    const responlayakikan = await axios.get(`${BASE_URL}/Kelayakan-perikanan`,{
      headers:{
        'Access-Control-Allow-Origin': '*',
      }
    });

    const todoItemslayakikan = responlayakikan.data;

    console.log(`GET: Here's the list of todos`, todoItemslayakikan);
    
    return todoItemslayakikan;
  } catch (errors) {
    console.error(errors);
  }
};
const createTodoElementlayakikan = dataread => {
  const todoElementlayakikan = document.createElement('li');todoElementlayakikan.appendChild(document.createTextNode(todoItemslayakikan.Kelayakan));

  return todoElementlayakikan;
};

const updateTodoListlayakikan = todoItemslayakikan => {
  const todoListlayakikan = document.querySelector('ul');
  todoListlayakikan.appendChild(document.createElement('br'))
  todoListlayakikan.appendChild(document.createElement('br'))
  todoListlayakikan.appendChild(document.createElement('li').appendChild(document.createTextNode("Kelayakan air untuk perikanan : " + todoItemslayakikan.Kelayakan)))
  if (todoItemslayakikan) {
    // todoList.appendChild(createTodoElement(todoItems));
    
  }
};

const getlastread = async () => {
    try {
      const response = await axios.get(`${BASE_URL}/last-read`,{
        headers:{
          'Access-Control-Allow-Origin': '*',
        }
      });
  
      const todoItems = response.data;
  
      console.log(`GET: Here's the list of todos`, todoItems);
      
      return todoItems;
    } catch (errors) {
      console.error(errors);
    }
  };
  const createTodoElement = dataread => {
    const todoElement = document.createElement('li');todoElement.appendChild(document.createTextNode(todoItems.lastph));
  
    return todoElement;
  };
  
  const updateTodoList = todoItems => {
    const todoList = document.querySelector('ul');
    todoList.appendChild(document.createElement('li').appendChild(document.createTextNode("Pembacaan sensor saat ini: ")))
    todoList.appendChild(document.createElement('br'))
    todoList.appendChild(document.createElement('br'))
    todoList.appendChild(document.createElement('li').appendChild(document.createTextNode("pH : " + todoItems.lastph)))
    todoList.appendChild(document.createElement('br'))
    todoList.appendChild(document.createElement('li').appendChild(document.createTextNode("Turbidity : " +todoItems.lastturb)))
    todoList.appendChild(document.createElement('br'))
    todoList.appendChild(document.createElement('li').appendChild(document.createTextNode("Dissolved Oxygen : "+todoItems.lastdissoxy)))
    todoList.appendChild(document.createElement('br'))
    todoList.appendChild(document.createElement('li').appendChild(document.createTextNode("Temperature : "+ todoItems.lastph)))
    todoList.appendChild(document.createElement('br'))
    todoList.appendChild(document.createElement('li').appendChild(document.createTextNode("Oxidation Reduction Potential : "+ todoItems.lastorp)))
    todoList.appendChild(document.createElement('br'))
    todoList.appendChild(document.createElement('li').appendChild(document.createTextNode("Conductivity : "+todoItems.lastcond)))
    if (todoItems) {
      // todoList.appendChild(createTodoElement(todoItems));
      
    }
  };
  const main = async () => {
    updateTodoList(await getlastread());
    updateTodoListlayakminum(await getkelayakanminum());
    updateTodoListlayaksanitasi(await getkelayakansanitasi());
    updateTodoListlayaktani(await getkelayakantani());
    updateTodoListlayakikan(await getkelayakanikan());
  };
  
  main();

