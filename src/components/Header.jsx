function Header(props)
{
    return(
        <>
      <div className='bg-black p-16'>
      <div className="bg-[#EFEFEF] p-10 border rounded-md">
        <h1 className="text-3xl font-medium">Hi {props.username}!</h1>
        <p>I help you manage your activities :)</p>
        </div>
        </div>
        </>
    )
}

export default Header