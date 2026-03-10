import { auth } from "./firebase.js";
import { 
  GoogleAuthProvider, 
  signInWithPopup, 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword, 
  sendPasswordResetEmail 
} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

const provider = new GoogleAuthProvider();

export function googleLogin() {
  return signInWithPopup(auth, provider)
    .then((result) => {
      console.log("User logged in with Google:", result.user);
      return result.user;
    })
    .catch((error) => {
      console.error("Google login failed:", error);
      throw error;
    });
}

export function emailLogin(email, password) {
  return signInWithEmailAndPassword(auth, email, password)
    .then((result) => {
      console.log("User logged in with email:", result.user);
      return result.user;
    })
    .catch((error) => {
      console.error("Email login failed:", error);
      throw error;
    });
}

export function emailSignup(email, password) {
  return createUserWithEmailAndPassword(auth, email, password)
    .then((result) => {
      console.log("User signed up with email:", result.user);
      return result.user;
    })
    .catch((error) => {
      console.error("Email signup failed:", error);
      throw error;
    });
}

export function resetPassword(email) {
  return sendPasswordResetEmail(auth, email)
    .then(() => {
      console.log("Password reset email sent to:", email);
    })
    .catch((error) => {
      console.error("Password reset failed:", error);
      throw error;
    });
}
