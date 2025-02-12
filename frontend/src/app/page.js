'use client'

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';

export default function Home() {

    const [flag, setFlag] = useState(0)

    return (
        <div className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
        
            {/* Component for create a new task */}
            <TaskForm
                flag={flag}
                setFlag={setFlag}
            />

             {/* Component for list the tasks */}
            <TaskList 
                flag={flag}
                setFlag={setFlag}
            />
        </div>

    );
}
