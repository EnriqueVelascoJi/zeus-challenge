'use client'

import { useState, useEffect } from 'react';


export default function TaskList({flag, setFlag}) {
    
    const url = "https://fastapi-example-ngas.onrender.com/v1/tasks"

    const [tasks, setTasks] = useState([])

    const toggleComplete = async(id) => {
        const singularURL = url + `/${id}`
        const taskToEdit = tasks.find(task => task.id === id)
        console.log(taskToEdit)
        const body = {
            is_completed: !taskToEdit.is_completed
        }
        
        try {
            const response = await fetch(singularURL, {
                method: 'PUT',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify(body)
            })
            const result = await response.json()
            if(result) {
                setFlag(Math.random())
            }

        } catch (error) {
            console.error("An unexpected error occurred", error)
        }
    };

    const deleteTask = async (id) => {
        const singularURL = url + `/${id}`
        
        try {
            const response = await fetch(singularURL, {
                method: 'DELETE',
                headers: {
                    'Content-type': 'application/json'
                },
            })
            const result = await response.json()
            if(result) {
                setFlag(Math.random())
            }

        } catch (error) {
            console.error("An unexpected error occurred", error)
        }
    };

    useEffect(() => {
        async function fetchTasks() {
          const res = await fetch(url)
          const data = await res.json()
          setTasks(data)
        }
        fetchTasks()
      }, [flag])

    return (
        <>
            <h2 className="text-2xl font-bold mt-6 mb-4">To-Do List</h2>
            <ul className="space-y-4">
                {tasks.map((task) => (
                <li
                    key={task.id}
                    className={`bg-gray-50 p-4 rounded-lg shadow flex justify-between items-center ${
                    task.is_completed ? 'line-through text-gray-400' : ''
                    }`}
                >
                    <div className="flex items-center">
                    <input
                        type="checkbox"
                        checked={task.is_completed}
                        onChange={() => toggleComplete(task.id)}
                        className="mr-4"
                    />
                    <div>
                        <h3 className="text-lg font-semibold">{task.title}</h3>
                        <p className="text-sm">{task.description}</p>
                    </div>
                    </div>
                    <button onClick={() => deleteTask(task.id)} className="text-red-500 hover:text-red-700">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                            <path strokeLinecap="round" strokeLinejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                        </svg>
                    </button>
                </li>
                ))}
            </ul>
        </>

    );
}
