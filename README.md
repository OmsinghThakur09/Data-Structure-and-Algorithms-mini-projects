# 🚀 Data Structures Mini Projects

A collection of practical, real-world applications demonstrating core data structures and algorithms through interactive command-line programs. Each project is built from scratch in Python to solidify understanding of fundamental computer science concepts.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [1. Text Editor with Undo/Redo](#1-text-editor-with-undoredo)
  - [2. Music Playlist Manager](#2-music-playlist-manager)
  - [3. Social Network Analyzer](#3-social-network-analyzer)
  - [4. City Route Planner](#4-city-route-planner)
  - [5. Bank Queue Simulation](#5-bank-queue-simulation)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Data Structures Implemented](#data-structures-implemented)
- [Algorithms Implemented](#algorithms-implemented)
- [Key Learnings](#key-learnings)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🎯 Overview

This repository contains **5 mini projects** that demonstrate the practical application of fundamental data structures:

- **Stack** → Text Editor with Undo/Redo
- **Doubly Linked List** → Music Playlist Manager
- **Graph** → Social Network Analyzer & City Route Planner
- **Queue & Priority Queue** → Bank Queue Simulation

Each project is:
- ✅ **Fully functional** with interactive CLI
- ✅ **Built from scratch** (custom implementations)
- ✅ **Well-documented** with clear code structure
- ✅ **Production-ready** with error handling and validation

---

## 📂 Projects

### 1️⃣ Text Editor with Undo/Redo

**📁 Directory**: `text_editor/`

**🎯 Purpose**: A command-line text editor demonstrating Stack data structure through undo/redo functionality.

**🏗️ Data Structure**: 
- **Stack** (LIFO - Last In First Out)
- Dual-stack architecture (Undo + Redo)

**✨ Key Features**:
- Write and delete text
- Undo operations (revert to previous state)
- Redo operations (restore undone changes)
- View current document state
- Track edit history

**⚙️ Technical Highlights**:
- Custom Stack implementation from scratch
- State preservation and restoration
- O(1) time complexity for all operations
- Memory-efficient operation tracking

**🚀 Run**:
```bash
cd text_editor
python text_editor.py
```

**📸 Example**:
Current text: ""
Write "Hello World"
Undo
Current text: "Hello"
Redo
Current text: "Hello World"
---

### 2️⃣ Music Playlist Manager

**📁 Directory**: `music_playlist/`

**🎯 Purpose**: A comprehensive music playlist management system with bidirectional navigation, shuffle, loop modes, and play history.

**🏗️ Data Structure**: 
- **Doubly Linked List** (for forward/backward navigation)
- Custom Node implementation with `prev` and `next` pointers

**✨ Key Features**:
- Add/remove songs with metadata (title, artist, duration)
- Play controls: play, pause, next, previous
- Jump to specific song by position
- Shuffle and reverse playlist
- Loop/repeat mode (circular behavior)
- Recently played history (last 10 songs)
- Search songs by title
- Playlist statistics and analytics

**⚙️ Technical Highlights**:
- Bidirectional traversal using doubly linked list
- O(1) navigation to previous/next songs
- Efficient insertion and deletion
- Separate linked list for play history
- Sample playlist with 8 classic rock songs

**🚀 Run**:
```bash
cd music_playlist
python music_playlist.py
```

**📸 Example**:
🎧 Playlist: My Awesome Mix (5 songs)
▶️ 1. 🎵 Bohemian Rhapsody - Queen (5:54)
2. 🎵 Stairway to Heaven - Led Zeppelin (8:02)
3. 🎵 Hotel California - Eagles (6:31)
---

### 3️⃣ Social Network Analyzer

**📁 Directory**: `social_network/`

**🎯 Purpose**: A graph-based social network simulation with friend recommendations, connection pathfinding, and community detection.

**🏗️ Data Structure**: 
- **Undirected Graph** (Adjacency List representation)
- **BFS** (Breadth-First Search) for pathfinding
- **DFS** (Depth-First Search) for community detection

**✨ Key Features**:
- Add/remove users and friendships
- Find mutual friends between users
- Friend suggestions based on mutual connections
- Shortest connection path (degrees of separation)
- Detect friend circles/communities (connected components)
- Most popular user identification
- Network statistics and analytics
- User search functionality

**⚙️ Technical Highlights**:
- Graph implementation using dictionary-based adjacency list
- BFS algorithm for shortest path: O(V + E)
- DFS algorithm for connected components: O(V + E)
- Priority-based friend recommendations
- Sample network with 8 users

**🚀 Run**:
```bash
cd social_network
python social_network.py
```

**📸 Example**:
🔍 Connection Path: Alice → Grace
Degrees of Separation: 3
Path: Alice → Bob → David → Grace
---

### 4️⃣ City Route Planner

**📁 Directory**: `city_route_planner/`

**🎯 Purpose**: A navigation system that finds optimal routes between cities using weighted graphs and Dijkstra's algorithm.

**🏗️ Data Structure**: 
- **Weighted Graph** (Adjacency List with edge weights)
- **Priority Queue** (Min-Heap) for Dijkstra's algorithm
- Dictionary for city metadata

**✨ Key Features**:
- Add/remove cities with population and country data
- Create bidirectional routes with distance weights
- **Dijkstra's algorithm** for shortest path calculation
- Find all possible paths between cities
- Nearest cities search functionality
- Route validation and existence checking
- Network statistics (total routes, distances)

**⚙️ Technical Highlights**:
- Implemented Dijkstra's shortest path algorithm
- Min-heap priority queue using Python's `heapq`
- O((V + E) log V) time complexity for pathfinding
- DFS for finding all paths
- Sample network with 10 major Indian cities
- Real distance data in kilometers

**🚀 Run**:
```bash
cd city_route_planner
python city_route_planner.py
```

**📸 Example**:
🗺️  Shortest Route: Mumbai → Kolkata
Total Distance: 1935 km
Route: Mumbai → Nagpur → Kolkata
---

### 5️⃣ Bank Queue Simulation

**📁 Directory**: `bank_queue_simulation/`

**🎯 Purpose**: A realistic bank simulation managing customer queues with priority handling, multiple service counters, and performance analytics.

**🏗️ Data Structure**: 
- **Priority Queue** (Min-Heap using `heapq`)
- **FIFO Queue** (Deque for regular customers)
- Dual-queue system (Priority + Regular)

**✨ Key Features**:
- Multiple customer types: VIP 💳, Senior 👴, Disabled ♿, Regular 👤
- 6 service types: Deposit, Withdrawal, Loan Application, etc.
- Multiple service counter management (dynamic add/remove)
- Smart customer assignment to available counters
- Priority-based queue processing
- Time-based service simulation
- Real-time wait time calculation
- Customer search by ID
- Comprehensive statistics (avg wait, counter utilization)

**⚙️ Technical Highlights**:
- Combined priority queue (heapq) and FIFO queue (deque)
- Tuple-based priority with tie-breaking: (priority, ID, customer)
- O(log n) enqueue/dequeue operations
- Real-time datetime-based simulation
- Resource utilization metrics
- Sample customer data loader

**🚀 Run**:
```bash
cd bank_queue_simulation
python bank_queue_simulation.py
```

**📸 Example**:
🏦 BANK QUEUE STATUS
Waiting Customers: 5
--- Service Counters (3) ---
🔴 Counter 1: Serving Bob Smith - 2.3 min left
🟢 Counter 2: Available ⭐
🔴 Counter 3: Serving Alice Johnson - 3.1 min left
--- Priority Queue (2) ---

💳 VIP: Frank Miller - Wait: 0.5 min
👴 Senior: Grace Lee - Wait: 0.3 min
---

## 🛠️ Technologies Used

**Language**: Python 3.6+

**Built-in Modules**:
- `collections` (deque, defaultdict)
- `heapq` (priority queue implementation)
- `datetime` (time simulation)
- `random` (shuffle functionality)
- `os` (CLI utilities)

**Design Patterns**:
- Object-Oriented Programming (OOP)
- Modular code architecture
- Separation of concerns

---

## 📥 Installation & Setup

### Prerequisites
- Python 3.6 or higher

### Clone Repository
```bash
git clone https://github.com/yourusername/data-structures-mini-projects.git
cd data-structures-mini-projects
```

### Run Any Project
```bash
# Example: Run Music Playlist Manager
cd music_playlist
python music_playlist.py
```

### No External Dependencies
All projects use Python standard library only - no `pip install` required!

---

## 🏗️ Data Structures Implemented

| Data Structure | Project | Implementation | Time Complexity |
|---------------|---------|----------------|-----------------|
| **Stack** | Text Editor | Custom class | O(1) all ops |
| **Doubly Linked List** | Music Playlist | Custom nodes | O(1) next/prev |
| **Graph (Adjacency List)** | Social Network | Dictionary | O(V + E) traversal |
| **Weighted Graph** | City Routes | Dictionary + weights | O((V+E)log V) Dijkstra |
| **Priority Queue** | Bank Simulation | heapq (min-heap) | O(log n) enqueue/dequeue |
| **FIFO Queue** | Bank Simulation | deque | O(1) all ops |
| **Hash Table** | All projects | Python dict | O(1) average lookup |

---

## 🧠 Algorithms Implemented

### Search & Traversal
- **Breadth-First Search (BFS)**: Social Network (shortest path)
- **Depth-First Search (DFS)**: Social Network (community detection), City Routes (all paths)

### Shortest Path
- **Dijkstra's Algorithm**: City Route Planner (weighted shortest path)
  - Time: O((V + E) log V)
  - Space: O(V)

### Sorting & Ordering
- **Priority Queue Operations**: Bank Queue (heapq)
- **Shuffle Algorithm**: Music Playlist (Fisher-Yates)

### Graph Algorithms
- **Connected Components**: Friend circles detection
- **Path Finding**: Degrees of separation
- **Mutual Friends**: Set intersection

---

## 📊 Complexity Analysis

### Time Complexities Achieved

| Operation | Data Structure | Complexity |
|-----------|---------------|------------|
| Stack Push/Pop | Stack | O(1) |
| List Next/Prev | Doubly Linked List | O(1) |
| Graph BFS/DFS | Graph | O(V + E) |
| Dijkstra's Algorithm | Weighted Graph | O((V + E) log V) |
| Priority Enqueue/Dequeue | Min-Heap | O(log n) |
| FIFO Enqueue/Dequeue | Deque | O(1) |

### Space Complexities

| Project | Space Complexity | Notes |
|---------|-----------------|-------|
| Text Editor | O(k) | k = number of states |
| Music Playlist | O(n) | n = number of songs |
| Social Network | O(V + E) | Adjacency list |
| City Routes | O(V + E) | Weighted adjacency list |
| Bank Queue | O(n) | n = customers |

---

## 💡 Key Learnings

### Data Structure Selection
- **Stack** for reversible operations (undo/redo)
- **Doubly Linked List** when bidirectional traversal needed
- **Graph** for modeling relationships and networks
- **Priority Queue** when order matters (priority-based processing)
- **FIFO Queue** for fair ordering (first-come-first-served)

### Algorithm Design
- BFS for **shortest path** in unweighted graphs
- DFS for **connectivity** and **cycle detection**
- Dijkstra for **shortest path** in weighted graphs
- Heap for **efficient priority** management

### Code Quality
- Input validation and error handling
- Modular, reusable code structure
- Clear variable naming and documentation
- Interactive CLI for user experience

---

## 🔮 Future Enhancements

### Across All Projects
- [ ] Add file save/load functionality (JSON/CSV)
- [ ] Create GUI versions using Tkinter
- [ ] Add unit tests (pytest)
- [ ] Implement visualization (networkx, matplotlib)

### Specific Projects
- [ ] **Text Editor**: Multi-file support, syntax highlighting
- [ ] **Music Playlist**: Spotify API integration
- [ ] **Social Network**: Graph visualization, ML recommendations
- [ ] **City Routes**: A* algorithm, real-time traffic
- [ ] **Bank Queue**: Multi-branch simulation, appointment system

---

## 📁 Repository Structure
Data_Structures/
│
├── Graph/
│   ├── graph.py
│   ├── weightedgraph.py
│   ├── route_planner.py
│   ├── social_network.py
│   ├── main_routeplanner.py
│   └── main_socialnetwork.py
│
├── LinkList/
│   ├── doubly_linkedlist.py
│   ├── Playlist.py
│   └── MusicPlaylistManager.py
│
├── Queue/
│   ├── bankqueuesystem.py
│   ├── customer.py
│   └── main.py
│
└── Stack/
    ├── stack.py
    ├── expression_converter.py
    ├── expression_evaluator.py
    ├── parentheses_checker.py
    └── simple_text_editor.py
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Built as part of learning **Data Structures and Algorithms**
- Inspired by real-world applications (Spotify, Facebook, Google Maps, Banking Systems)
- Special thanks to the open-source community for learning resources

---

## 📈 Project Stats

| Metric | Value |
|--------|-------|
| **Total Projects** | 5 |
| **Total Lines of Code** | ~2,050 |
| **Data Structures** | 7 |
| **Algorithms** | 6+ |
| **Features Implemented** | 60+ |
| **Programming Language** | Python |

---

## 🎓 Educational Value

These projects are ideal for:
- 📚 **Students** learning data structures
- 💼 **Interview preparation** (common DS/Algo problems)
- 🎯 **Portfolio projects** for job applications
- 🧠 **Understanding** practical applications of theory

---

## 🚀 Quick Start Guide

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/data-structures-mini-projects.git

# 2. Navigate to any project
cd data-structures-mini-projects/music_playlist

# 3. Run it!
python music_playlist.py

# 4. Explore the code and have fun! 🎉
```
