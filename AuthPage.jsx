import React, { useState } from 'react';
import { Mail, Lock, Eye, EyeOff, Github, Chrome, ArrowRight, UserPlus, LogIn } from 'lucide-react';

/**
 * Premium Auth Page Component
 * Features: Split-screen design, Google auth, Password visibility toggle, 
 * Responsive layout, and Modern SaaS aesthetic.
 */
const AuthPage = () => {
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);

    return (
        <div className="min-h-screen w-full bg-[#f8fafc] flex items-center justify-center p-4 sm:p-6 lg:p-8 font-sans selection:bg-indigo-100 relative overflow-hidden">
            {/* Background Decorative Elements */}
            <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-indigo-100/50 rounded-full blur-3xl animate-pulse"></div>
            <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-100/50 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }}></div>
            
            <div className="max-w-7xl w-full grid grid-cols-1 lg:grid-cols-2 gap-0 overflow-hidden rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.1)] relative z-10 border border-white/20">
                
                {/* LEFT CARD: SIGN UP */}
                <div className="bg-white/80 backdrop-blur-xl p-8 sm:p-12 flex flex-col items-center justify-center border-r border-gray-100">
                    {/* Illustration Area */}
                    <div className="mb-8 w-full max-w-[280px] aspect-video bg-gradient-to-br from-indigo-50 to-blue-50 rounded-2xl flex items-center justify-center relative group overflow-hidden border border-indigo-100/50 shadow-inner">
                        <UserPlus className="w-16 h-16 text-indigo-500 group-hover:scale-110 transition-transform duration-500" />
                        <div className="absolute -bottom-2 -right-2 w-16 h-16 bg-white rounded-full shadow-lg flex items-center justify-center border border-indigo-50">
                            <div className="w-10 h-1 bg-indigo-100 rounded-full overflow-hidden">
                                <div className="w-2/3 h-full bg-indigo-500 animate-progress"></div>
                            </div>
                        </div>
                    </div>

                    <div className="w-full text-center lg:text-left">
                        <h2 className="text-3xl font-extrabold text-gray-900 mb-2 tracking-tight">Create Account</h2>
                        <p className="text-gray-500 font-medium mb-8">Join Resume Classifier to boost your career</p>
                    </div>

                    <form className="w-full space-y-4" onSubmit={(e) => e.preventDefault()}>
                        {/* Email Field */}
                        <div className="relative group">
                            <label className="block text-sm font-semibold text-gray-700 mb-1.5 ml-1">Email Address</label>
                            <div className="relative">
                                <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 group-focus-within:text-indigo-500 transition-colors" />
                                <input 
                                    type="email" 
                                    placeholder="name@company.com"
                                    className="w-full pl-12 pr-4 py-3.5 bg-gray-50/50 border border-gray-200 rounded-xl focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 outline-none transition-all placeholder:text-gray-400 font-medium"
                                />
                            </div>
                        </div>

                        {/* Password Field */}
                        <div className="relative group">
                            <label className="block text-sm font-semibold text-gray-700 mb-1.5 ml-1">Password</label>
                            <div className="relative">
                                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 group-focus-within:text-indigo-500 transition-colors" />
                                <input 
                                    type={showPassword ? "text" : "password"} 
                                    placeholder="••••••••"
                                    className="w-full pl-12 pr-12 py-3.5 bg-gray-50/50 border border-gray-200 rounded-xl focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 outline-none transition-all placeholder:text-gray-400 font-medium"
                                />
                                <button 
                                    type="button"
                                    onClick={() => setShowPassword(!showPassword)}
                                    className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-indigo-500 transition-colors"
                                >
                                    {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                                </button>
                            </div>
                        </div>

                        {/* Confirm Password Field */}
                        <div className="relative group">
                            <label className="block text-sm font-semibold text-gray-700 mb-1.5 ml-1">Confirm Password</label>
                            <div className="relative">
                                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 group-focus-within:text-indigo-500 transition-colors" />
                                <input 
                                    type={showConfirmPassword ? "text" : "password"} 
                                    placeholder="••••••••"
                                    className="w-full pl-12 pr-12 py-3.5 bg-gray-50/50 border border-gray-200 rounded-xl focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 outline-none transition-all placeholder:text-gray-400 font-medium"
                                />
                                <button 
                                    type="button"
                                    onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                                    className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-indigo-500 transition-colors"
                                >
                                    {showConfirmPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                                </button>
                            </div>
                        </div>

                        <button className="w-full py-4 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white font-bold rounded-xl shadow-[0_10px_20px_rgba(79,70,229,0.3)] hover:shadow-[0_15px_30px_rgba(79,70,229,0.4)] active:scale-[0.98] transition-all flex items-center justify-center gap-2 group">
                            Create Account
                            <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                        </button>
                    </form>

                    <div className="w-full flex items-center my-8">
                        <div className="flex-1 h-px bg-gray-100"></div>
                        <span className="px-4 text-xs font-bold text-gray-400 uppercase tracking-widest">OR SIGN UP WITH</span>
                        <div className="flex-1 h-px bg-gray-100"></div>
                    </div>

                    <button className="w-full py-3.5 bg-white border border-gray-200 hover:border-indigo-300 hover:bg-gray-50 text-gray-700 font-semibold rounded-xl transition-all flex items-center justify-center gap-3">
                        <svg className="w-5 h-5" viewBox="0 0 24 24">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/>
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.66l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
                        </svg>
                        Sign up with Google
                    </button>

                    <p className="mt-8 text-center text-sm font-medium text-gray-500">
                        Already have an account? <button className="text-indigo-600 font-bold hover:underline">Sign In</button>
                    </p>
                </div>

                {/* RIGHT CARD: SIGN IN */}
                <div className="bg-[#0f172a] p-8 sm:p-12 flex flex-col items-center justify-center relative group">
                    {/* Dark Card Glow Effect */}
                    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[80%] h-[80%] bg-indigo-500/10 rounded-full blur-[100px] pointer-events-none"></div>
                    
                    {/* Illustration Area */}
                    <div className="mb-8 w-full max-w-[280px] aspect-video bg-white/5 rounded-2xl flex items-center justify-center relative overflow-hidden border border-white/10 shadow-2xl">
                        <LogIn className="w-16 h-16 text-indigo-400 group-hover:scale-110 transition-transform duration-500" />
                        <div className="absolute top-0 right-0 p-4">
                            <div className="w-10 h-10 rounded-lg bg-indigo-500/20 flex items-center justify-center border border-indigo-500/30">
                                <Lock className="w-5 h-5 text-indigo-400" />
                            </div>
                        </div>
                    </div>

                    <div className="w-full text-center lg:text-left relative z-10">
                        <h2 className="text-3xl font-extrabold text-white mb-2 tracking-tight">Welcome Back</h2>
                        <p className="text-indigo-200/60 font-medium mb-8">Sign in to continue your journey</p>
                    </div>

                    <form className="w-full space-y-4 relative z-10" onSubmit={(e) => e.preventDefault()}>
                        {/* Email Field */}
                        <div className="relative group">
                            <label className="block text-sm font-semibold text-indigo-200/80 mb-1.5 ml-1">Email Address</label>
                            <div className="relative">
                                <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-indigo-300/40 group-focus-within:text-indigo-400 transition-colors" />
                                <input 
                                    type="email" 
                                    placeholder="name@company.com"
                                    className="w-full pl-12 pr-4 py-3.5 bg-white/5 border border-white/10 rounded-xl focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-400 outline-none transition-all placeholder:text-indigo-300/20 text-white font-medium"
                                />
                            </div>
                        </div>

                        {/* Password Field */}
                        <div className="relative group">
                            <div className="flex justify-between items-center mb-1.5 px-1">
                                <label className="text-sm font-semibold text-indigo-200/80">Password</label>
                                <button className="text-xs font-bold text-indigo-400 hover:text-indigo-300 transition-colors">Forgot Password?</button>
                            </div>
                            <div className="relative">
                                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-indigo-300/40 group-focus-within:text-indigo-400 transition-colors" />
                                <input 
                                    type={showPassword ? "text" : "password"} 
                                    placeholder="••••••••"
                                    className="w-full pl-12 pr-12 py-3.5 bg-white/5 border border-white/10 rounded-xl focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-400 outline-none transition-all placeholder:text-indigo-300/20 text-white font-medium"
                                />
                                <button 
                                    type="button"
                                    onClick={() => setShowPassword(!showPassword)}
                                    className="absolute right-4 top-1/2 -translate-y-1/2 text-indigo-300/40 hover:text-indigo-400 transition-colors"
                                >
                                    {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                                </button>
                            </div>
                        </div>

                        <button className="w-full py-4 bg-gradient-to-r from-indigo-500 to-purple-500 hover:from-indigo-600 hover:to-purple-600 text-white font-bold rounded-xl shadow-[0_10px_30px_rgba(79,70,229,0.2)] hover:shadow-[0_15px_40px_rgba(79,70,229,0.3)] active:scale-[0.98] transition-all flex items-center justify-center gap-2 group mt-4">
                            Sign In
                            <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                        </button>
                    </form>

                    <div className="w-full flex items-center my-8 relative z-10">
                        <div className="flex-1 h-px bg-white/10"></div>
                        <span className="px-4 text-xs font-bold text-indigo-300/40 uppercase tracking-widest">OR CONTINUE WITH</span>
                        <div className="flex-1 h-px bg-white/10"></div>
                    </div>

                    <button className="w-full py-3.5 bg-white/5 border border-white/10 hover:border-indigo-500/30 hover:bg-white/10 text-white font-semibold rounded-xl transition-all flex items-center justify-center gap-3 relative z-10">
                        <svg className="w-5 h-5" viewBox="0 0 24 24">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/>
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.66l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
                        </svg>
                        Sign in with Google
                    </button>

                    <p className="mt-8 text-center text-sm font-medium text-indigo-200/60 relative z-10">
                        Don't have an account? <button className="text-indigo-400 font-bold hover:underline">Sign Up</button>
                    </p>
                </div>
            </div>

            {/* Global Smooth Transitions Styles */}
            <style jsx>{`
                @keyframes progress {
                    0% { transform: translateX(-100%); }
                    100% { transform: translateX(100%); }
                }
                .animate-progress {
                    animation: progress 2s infinite ease-in-out;
                }
            `}</style>
        </div>
    );
};

export default AuthPage;
