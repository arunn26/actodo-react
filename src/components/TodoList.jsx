import TodoItem from "./TodoItem"

function TodoList(props)
{
    const activityArr= props.activityArr
    const setActivityArr = props.setActivityArr
    

    return(
        <div className="bg-[#BDB4EA] border rounded-md p-2 flex-grow">
        <h1 className="text-2xl font-medium">Today's Activity</h1>
        {activityArr.length===0?<p>You haven't added any activity yet</p>:""}
        {
            activityArr.map(function(item,index){
                return <TodoItem activityArr={activityArr} id={item.id} setActivityArr={setActivityArr} index={index} activity={item.activity}/>
            })
        }

        </div>
    )
}
export default TodoList