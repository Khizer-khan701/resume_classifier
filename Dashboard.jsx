import React from "react";
import { 
  LayoutDashboard, 
  FileText, 
  Trophy, 
  Zap, 
  Upload, 
  Search, 
  Bell, 
  User, 
  LogOut, 
  TrendingUp, 
  CheckCircle, 
  AlertCircle, 
  MoreVertical,
  Briefcase,
  Star,
  Settings
} from "lucide-react";

// --- Components ---

const Navbar = () => (
  <nav className="bg-white/80 backdrop-blur-md sticky top-0 z-50 border-b border-gray-100 px-6 py-4 flex items-center justify-between">
    <div className="flex items-center gap-8">
      <div className="flex items-center gap-2 group cursor-pointer">
        <div className="w-9 h-9 bg-indigo-600 rounded-lg flex items-center justify-center shadow-lg shadow-indigo-200 group-hover:rotate-6 transition-transform">
          <FileText className="w-5 h-5 text-white" />
        </div>
        <span className="text-xl font-black text-gray-900 tracking-tighter">Resume Classifier</span>
      </div>
      
      <div className="hidden md:flex items-center gap-1">
        {["Dashboard", "My Resumes", "Career Tools"].map((item, idx) => (
          <button 
            key={item} 
            className={`px-4 py-2 rounded-xl text-sm font-bold transition-all ${
              idx === 0 ? "bg-indigo-50 text-indigo-600" : "text-gray-500 hover:bg-gray-50 hover:text-gray-900"
            }`}
          >
            {item}
          </button>
        ))}
      </div>
    </div>

    <div className="flex items-center gap-4">
      <div className="relative hidden sm:block">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
        <input 
          type="text" 
          placeholder="Search resumes..." 
          className="pl-10 pr-4 py-2 bg-gray-50 border border-gray-100 rounded-xl text-sm outline-none focus:ring-2 focus:ring-indigo-500/10 focus:border-indigo-500 transition-all w-64"
        />
      </div>
      <button className="p-2 text-gray-400 hover:text-gray-900 transition-colors relative">
        <Bell className="w-5 h-5" />
        <span className="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-white"></span>
      </button>
      <div className="h-8 w-px bg-gray-100 mx-2"></div>
      <button className="flex items-center gap-2 pl-2 pr-1 py-1 rounded-full hover:bg-gray-50 transition-colors group">
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white text-xs font-bold shadow-md">
          JD
        </div>
        <LogOut className="w-4 h-4 text-gray-400 group-hover:text-red-500 transition-colors" />
      </button>
    </div>
  </nav>
);

const StatCard = ({ icon: Icon, label, value, trend, colorClass }) => (
  <div className="bg-white p-6 rounded-[2rem] border border-gray-50 shadow-[0_8px_30px_rgb(0,0,0,0.02)] hover:shadow-[0_20px_40px_rgba(0,0,0,0.04)] hover:-translate-y-1 transition-all group">
    <div className="flex justify-between items-start mb-4">
      <div className={`p-3 rounded-2xl ${colorClass} bg-opacity-10 transition-transform group-hover:scale-110`}>
        <Icon className={`w-6 h-6 ${colorClass.replace('bg-', 'text-')}`} />
      </div>
      {trend && (
        <span className="text-[10px] font-black px-2 py-1 rounded-full bg-green-50 text-green-600 uppercase tracking-wider">
          {trend}
        </span>
      )}
    </div>
    <p className="text-gray-400 text-sm font-bold mb-1">{label}</p>
    <h3 className="text-3xl font-black text-gray-900 tracking-tight">{value}</h3>
  </div>
);

const RecentResumeRow = ({ name, date, score, status }) => {
  const getStatusStyle = (status) => {
    switch(status) {
      case 'Good': return 'bg-green-50 text-green-600 border-green-100';
      case 'Average': return 'bg-yellow-50 text-yellow-600 border-yellow-100';
      case 'Needs Improvement': return 'bg-red-50 text-red-600 border-red-100';
      default: return 'bg-gray-50 text-gray-600 border-gray-100';
    }
  };

  return (
    <tr className="group hover:bg-gray-50/50 transition-colors border-b border-gray-50 last:border-0">
      <td className="py-5 px-4">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-indigo-50 flex items-center justify-center">
            <FileText className="w-5 h-5 text-indigo-600" />
          </div>
          <div>
            <p className="font-bold text-gray-900 group-hover:text-indigo-600 transition-colors">{name}</p>
            <p className="text-xs text-gray-400 font-medium">PDF • 2.4 MB</p>
          </div>
        </div>
      </td>
      <td className="py-5 px-4 text-sm font-bold text-gray-500">{date}</td>
      <td className="py-5 px-4">
        <div className="flex items-center gap-2">
          <div className="flex-1 h-1.5 w-16 bg-gray-100 rounded-full overflow-hidden">
            <div className="h-full bg-indigo-500 rounded-full" style={{ width: `${score}%` }}></div>
          </div>
          <span className="text-sm font-black text-gray-900">{score}</span>
        </div>
      </td>
      <td className="py-5 px-4">
        <span className={`px-3 py-1 rounded-full text-[11px] font-black border ${getStatusStyle(status)} uppercase tracking-wider`}>
          {status}
        </span>
      </td>
      <td className="py-5 px-4 text-right">
        <button className="p-2 hover:bg-white hover:shadow-md rounded-lg transition-all">
          <MoreVertical className="w-4 h-4 text-gray-400" />
        </button>
      </td>
    </tr>
  );
};

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-[#f8fafc] font-sans selection:bg-indigo-100 selection:text-indigo-600">
      <Navbar />

      <main className="max-w-7xl mx-auto px-6 py-10">
        
        {/* HERO SECTION */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-12">
          <div>
            <h1 className="text-4xl font-black text-gray-900 tracking-tight mb-2">Welcome back, John! 👋</h1>
            <p className="text-gray-500 font-medium text-lg">Track your resumes, ATS scores, and optimization progress.</p>
          </div>
          <button className="flex items-center justify-center gap-2 bg-gradient-to-r from-indigo-600 via-indigo-600 to-purple-600 text-white font-bold px-8 py-4 rounded-2xl shadow-xl shadow-indigo-100 hover:brightness-110 active:scale-95 transition-all group">
            <Upload className="w-5 h-5 group-hover:-translate-y-1 transition-transform" />
            Upload New Resume
          </button>
        </div>

        {/* STATS GRID */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          <StatCard icon={FileText} label="Total Resumes" value="12" trend="+3 this month" colorClass="bg-indigo-500" />
          <StatCard icon={Trophy} label="Avg ATS Score" value="78%" trend="Good" colorClass="bg-purple-500" />
          <StatCard icon={Star} label="Best Score" value="94" trend="Senior" colorClass="bg-blue-500" />
          <StatCard icon={Zap} label="Skills Detected" value="45" trend="Top 5%" colorClass="bg-emerald-500" />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* CHART & TABLE AREA (Left 2/3) */}
          <div className="lg:col-span-2 space-y-8">
            
            {/* ANALYTICS CARD */}
            <div className="bg-white p-8 rounded-[2.5rem] border border-gray-50 shadow-[0_8px_30px_rgb(0,0,0,0.02)]">
              <div className="flex items-center justify-between mb-8">
                <div>
                  <h3 className="text-xl font-black text-gray-900 tracking-tight">ATS Score Overview</h3>
                  <p className="text-sm text-gray-400 font-medium">Your score progression over time</p>
                </div>
                <select className="bg-gray-50 border-none rounded-xl px-4 py-2 text-xs font-bold text-gray-500 outline-none">
                  <option>Last 6 Months</option>
                  <option>Last Year</option>
                </select>
              </div>
              
              {/* Fake Chart Placeholder */}
              <div className="h-64 relative flex items-end justify-between gap-4 pt-4">
                {[45, 60, 55, 80, 75, 94].map((h, i) => (
                  <div key={i} className="flex-1 group relative">
                    <div 
                      className="w-full bg-gradient-to-t from-indigo-50 to-indigo-500/20 group-hover:from-indigo-100 group-hover:to-indigo-500/40 rounded-t-2xl transition-all relative overflow-hidden" 
                      style={{ height: `${h}%` }}
                    >
                      <div className="absolute inset-0 bg-indigo-500/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    </div>
                    <div className="text-[10px] font-bold text-gray-400 text-center mt-3 lowercase">
                      {['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'][i]}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* RECENT RESUMES */}
            <div className="bg-white rounded-[2.5rem] border border-gray-50 shadow-[0_8px_30px_rgb(0,0,0,0.02)] overflow-hidden">
              <div className="p-8 flex items-center justify-between border-b border-gray-50">
                <h3 className="text-xl font-black text-gray-900 tracking-tight">Recent Resumes</h3>
                <button className="text-sm font-bold text-indigo-600 hover:text-indigo-800 transition-colors">View All</button>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full text-left">
                  <thead>
                    <tr className="bg-gray-50/50">
                      <th className="py-4 px-6 text-[10px] font-black text-gray-400 uppercase tracking-widest">Resume Name</th>
                      <th className="py-4 px-4 text-[10px] font-black text-gray-400 uppercase tracking-widest">Upload Date</th>
                      <th className="py-4 px-4 text-[10px] font-black text-gray-400 uppercase tracking-widest">ATS Score</th>
                      <th className="py-4 px-4 text-[10px] font-black text-gray-400 uppercase tracking-widest">Status</th>
                      <th className="py-4 px-4 text-[10px] font-black text-gray-400 uppercase tracking-widest"></th>
                    </tr>
                  </thead>
                  <tbody>
                    <RecentResumeRow name="Software_Eng_Senior.pdf" date="Mar 10, 2026" score={94} status="Good" />
                    <RecentResumeRow name="Frontend_Dev_React.pdf" date="Mar 08, 2026" score={82} status="Good" />
                    <RecentResumeRow name="Data_Scientist_V1.pdf" date="Feb 28, 2026" score={58} status="Average" />
                    <RecentResumeRow name="Generic_Resume_Old.pdf" date="Feb 15, 2026" score={42} status="Needs Improvement" />
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          {/* SIDEBAR AREA (Right 1/3) */}
          <div className="space-y-8">
            
            {/* AI SUGGESTIONS PANEL */}
            <div className="bg-gradient-to-br from-indigo-600 to-purple-700 p-8 rounded-[2.5rem] text-white shadow-2xl shadow-indigo-200 relative overflow-hidden group">
              <div className="absolute top-[-10%] right-[-10%] w-32 h-32 bg-white/10 rounded-full blur-2xl group-hover:scale-150 transition-transform duration-700"></div>
              
              <div className="relative z-10">
                <div className="w-12 h-12 bg-white/20 rounded-2xl flex items-center justify-center mb-6 backdrop-blur-md">
                  <Zap className="w-6 h-6 text-yellow-300" />
                </div>
                <h3 className="text-2xl font-black mb-2 tracking-tight">AI Insights</h3>
                <p className="text-white/70 font-medium text-sm mb-8 leading-relaxed">Personalized tips to boost your ATS viability by 30%.</p>
                
                <div className="space-y-4">
                  {[
                    "Add more quantified achievements",
                    "Include 5+ Python keywords",
                    "Improve summary impact",
                    "Strengthen Technical section"
                  ].map((tip, i) => (
                    <div key={i} className="flex items-start gap-3 bg-white/10 p-4 rounded-2xl backdrop-blur-sm border border-white/10 hover:bg-white/20 transition-all cursor-default group/item">
                      <div className="mt-1">
                        <CheckCircle className="w-4 h-4 text-emerald-400 group-hover/item:scale-125 transition-transform" />
                      </div>
                      <span className="text-sm font-bold tracking-tight">{tip}</span>
                    </div>
                  ))}
                </div>

                <button className="w-full mt-8 py-4 bg-white text-indigo-600 font-black rounded-xl hover:bg-gray-50 transition-colors shadow-lg shadow-black/10">
                  Try Optimization Tool
                </button>
              </div>
            </div>

            {/* CAREER TOOLS AD */}
            <div className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 bg-blue-50 rounded-2xl flex items-center justify-center">
                  <Briefcase className="w-6 h-6 text-blue-600" />
                </div>
                <div>
                  <h4 className="font-black text-gray-900 leading-tight">Career Toolkit</h4>
                  <p className="text-xs text-gray-400 font-bold uppercase tracking-widest">New Features</p>
                </div>
              </div>
              
              <div className="space-y-3">
                <button className="w-full flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 transition-all group">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-lg bg-indigo-50 flex items-center justify-center">
                      <FileText className="w-4 h-4 text-indigo-500" />
                    </div>
                    <span className="text-sm font-bold text-gray-700">Cover Letter Pro</span>
                  </div>
                  <TrendingUp className="w-4 h-4 text-gray-300 group-hover:text-indigo-400 transition-colors" />
                </button>
                <button className="w-full flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 transition-all group">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-lg bg-orange-50 flex items-center justify-center">
                      <AlertCircle className="w-4 h-4 text-orange-500" />
                    </div>
                    <span className="text-sm font-bold text-gray-700">Interview Prep AI</span>
                  </div>
                  <TrendingUp className="w-4 h-4 text-gray-300 group-hover:text-orange-400 transition-colors" />
                </button>
              </div>
            </div>

          </div>
        </div>

      </main>
    </div>
  );
}
