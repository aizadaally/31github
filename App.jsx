import React, { useState, useEffect, useRef } from 'react';
function App() {


  class App extends Component {
    constructor(props) {
      super(props);
      this.state = {
        viewIn: false,
        activeItem: {
          name: "",
          phone_number: "",
          email: "",
          gender: "",
          department: "",
          in: false
        },
        staffList: [],
        modal: false // Initialize modal state
      };
    }
  
    // Add componentDidMount()
    componentDidMount() {
      this.refreshList();
    }
  
    refreshList = () => {
      axios
        .get("http://localhost:8000/api/staff/", {
          headers: {
            // Add your authorization header here if needed
            // 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
  
           'Authorization' : '4b360269c55a9b66d6ab324361d58c4a536d5f24'
          }
        })
        .then(res => this.setState({ staffList: res.data }))
        .catch(err => console.log(err));
    };
  
    displayIn = status => {
      this.setState({ viewIn: status });
    };
  
    renderTabList = () => {
      return (
        <div className="my-5 tab-list">
          <span
            onClick={() => this.displayIn(true)}
            className={this.state.viewIn ? "active" : ""}
          >
            In
          </span>
          <span
            onClick={() => this.displayIn(false)}
            className={this.state.viewIn ? "" : "active"}
          >
            Out
          </span>
        </div>
      );
    };
  
    renderItems = () => {
      const { viewIn, staffList } = this.state;
      const newItems = staffList.filter(item => item.in === viewIn);
  
      return newItems.map(item => (
        <li
          key={item.id}
          className="list-group-item d-flex justify-content-between align-items-center"
        >
          <span className={`todo-name mr-2 ${viewIn ? "In-todo" : ""}`}>
            {item.name}
          </span>
          <span>
            <button
              onClick={() => this.editItem(item)}
              className="btn btn-secondary mr-2"
            >
              Edit
            </button>
            <button
              onClick={() => this.handleDelete(item)}
              className="btn btn-danger"
            >
              Delete
            </button>
          </span>
        </li>
      ));
    };
  
    toggle = () => {
      this.setState({ modal: !this.state.modal });
    };
  
    handleSubmit = item => {
      this.toggle();
      if (item.id) {
        axios
          .put(`http://localhost:8000/api/staff/${item.id}/`, item, {
            headers: {
              // Add your authorization header here if needed
              // 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
              'Authorization' : '4b360269c55a9b66d6ab324361d58c4a536d5f24'
  
  
            }
          })
          .then(res => this.refreshList());
      } else {
        axios
          .post("http://localhost:8000/api/staff/", item, {
            headers: {
              // Add your authorization header here if needed
              // 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
              'Authorization' : '4b360269c55a9b66d6ab324361d58c4a536d5f24'
            }
          })
          .then(res => this.refreshList());
      }
    };
  
    handleDelete = item => {
      axios
        .delete(`http://localhost:8000/api/staffdelete/${item.id}/`, {
          headers: {
            // Add your authorization header here if needed
            // 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
            'Authorization' : '4b360269c55a9b66d6ab324361d58c4a536d5f24'
          }
        })
        .then(res => this.refreshList());
    };
  
    createItem = () => {
      const item = {
        name: "",
        phone_number: "",
        email: "",
        gender: "",
        department: "",
        in: false
      };
      this.setState({ activeItem: item, modal: !this.state.modal });
    };
  
    editItem = item => {
      this.setState({ activeItem: item, modal: !this.state.modal });
    };
  
    render() {
      return (
        <main className="content">
          <h1 className="text-black text-uppercase text-center my-4">UCA in&Out</h1>
          <div className="row ">
            <div className="col-md-6 col-sm-10 mx-auto p-0">
              <div className="card p-3">
                <div className="">
                  <button onClick={this.createItem} className="btn btn-primary">
                    Add staff
                  </button>
                </div>
                {this.renderTabList()}
                <ul className="list-group list-group-flush">
                  {this.renderItems()}
                </ul>
              </div>
            </div>
          </div>
          {this.state.modal && (
            <Modal
              activeItem={this.state.activeItem}
              toggle={this.toggle}
              onSave={this.handleSubmit}
            />
          )}
        </main>
      );
    }
  }
  // const [department, setDepartment] = useState([])
  // const [staff, setStaff] = useState([])
  // const [record, setRecord] = useState([]) 

  // useEffect(() => {
  //   getData()
  // }, []) 


  // const homeRef = useRef(null)
  // const departmentRef = useRef(null)
  // const staffRef = useRef(null)
  // const recordRef = useRef(null)

  // const getData = async () => {
  //   const departmentResponse = await fetch('api/department/')
  //   const departmentData = await departmentResponse.json()
  //   setDepartment(departmentData)

  //   const stafftResponse = await fetch('api/staff/')
  //   const staffData = await stafftResponse.json()
  //   setStaff(staffData)

  //   const recordResponse = await fetch('api/record/')
  //   const recorfData = await recordResponse.json()
  //   setRecord(recordData)
   
  //   console.log(departmentData)
  //   console.log(staffData)
  //   console.log(recordData)
  // }

  
  
  
  
  
  
  
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}`, {headers: {"Authorization": "Token 4b360269c55a9b66d6ab324361d58c4a536d5f24"}});
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []); // Empty dependency array to run the effect only once when the component mounts




  return (
    <>
      <div>
        {/* Render your data here */}
        {data.map(item => (
          <p key={item.id}>{item.name}</p>
        ))}
      </div>
    </>
  );
}

export default App;
