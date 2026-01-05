import { Routes, Route } from "react-router-dom";

import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import Home from "./components/Home/Home";

function App() {
  return (
    <Routes>
      {/* Home page */}
      <Route path="/" element={<Home />} />

      {/* Login page */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Register page */}
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;
