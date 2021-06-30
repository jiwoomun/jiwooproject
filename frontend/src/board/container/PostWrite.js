import React,{useState} from 'react'
import './PostWrite.css'
import { postWrite } from 'api'

const PostWrite = () => {
    
    const  [post, setPost] = useState( {
      title: '',
      content:''
    })

    const {title, content} = post

    const handleClick = e => {
      e.preventDefault()
    }

    const handleSubmit = e =>{
      e.preventDefault()
      postWrite({...post})
      .then()
      .catch()
    }

    const handleChange = e =>{
      const {name, value} = e.target
      setPost({
        ...post,
        [name] : value
      })
    }


    return (<>
    <div className="PostWrite">
    <form onSubmit={handleSubmit} method="get" style={{border:"1px solid #ccc"}}>
      
  <div className="container">
    <h1>게시글 쓰기</h1>
    <p>Please fill in this form to create an account.</p>
    <hr/>

    <label for="title"><b>title</b></label>
    <input type="text" placeholder="Enter title" onChange={handleChange} name="title" value={title} required/>

    <label for="content"><b>content</b></label>
    <input type="text" placeholder="Enter content" onChange={handleChange} name="content" value={content} required/>

    
    <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

    <div class="clearfix">
    <button type="submit" className="signupbtn">Post</button>
    <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>

    </div>
  </div>
</form>
</div>
</>)
}

export default PostWrite