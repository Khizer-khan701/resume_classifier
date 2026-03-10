import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-analytics.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDUI_xLud7fA6NVc39qx-2vgntcEuiZj4w",
  authDomain: "resume-classifier-ef2f2.firebaseapp.com",
  projectId: "resume-classifier-ef2f2",
  storageBucket: "resume-classifier-ef2f2.firebasestorage.app",
  messagingSenderId: "345936452002",
  appId: "1:345936452002:web:81ad353a4810adbea67afb",
  measurementId: "G-5B9GW919R8"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const analytics = getAnalytics(app);

