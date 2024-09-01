import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import { setNectaryRegistry } from "@nectary/components/utils";
import "@nectary/components/input";

setNectaryRegistry(window.customElements);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <sinch-input />
    <App />
  </React.StrictMode>
);
