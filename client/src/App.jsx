import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css";
import Main from "./pages/Landing page/Main";


const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* <Route path={"/"} element={<Main />}/>
        <Route path="/" element={<LandingPage />} />
        <Route path="/contact-us" element={<ContactUsPage />} />
        <Route path="/products" element={<ProductsPage />}>
          <Route path="/" element={<ProductsList />} />
          <Route path=":productId" element={<ProductDetailPage />} />
        </Route> */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;

const root = createRoot(document.getElementById("root"));
root.render(<App />);