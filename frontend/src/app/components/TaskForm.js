'use client'

import { useState, useEffect } from 'react';

export default function TaskForm({flag, setFlag}) {
    
    const url = "https://fastapi-example-ngas.onrender.com/v1/tasks"

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');


    const addTask = async (e) => {
        e.preventDefault();
        const newTask = {
            title,
            description
        }
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify(newTask)
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
        setTitle('')
        setDescription('')
      }, [flag])
    return (
        <>
        <h2 className="text-2xl font-bold mb-4">Add a New Task</h2>
        <form onSubmit={addTask}>
            <div className="mb-4">
            <label htmlFor="title" className="block text-sm font-medium text-gray-700">
                Title
            </label>
            <input
                type="text"
                id="title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                placeholder="Task title"
                required
            />
            </div>
            <div className="mb-4">
            <label htmlFor="description" className="block text-sm font-medium text-gray-700">
                Description
            </label>
            <textarea
                id="description"
                rows="3"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                placeholder="Task description"
            ></textarea>
            </div>
            <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600"
            >
            Add Task
            </button>
        </form>
        </>

    );
}
