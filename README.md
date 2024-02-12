# War of Wands Match Statistics Tracker

Welcome to the War of Wands Match Statistics Tracker! This web application is designed to help players and enthusiasts of the "War of Wands" keep track of match statistics, analyze gameplay trends, and enhance their gaming experience. Whether you're a casual player looking to improve your skills or a competitive gamer aiming to dominate the leaderboards, this tool is for you.

## War of Wands Absolutely Does Not Exist

Let me be real with you, my Github is real sad and I need to put something fun on it. This experiment is to mess around with a few technologies I'd had my eye on and work on a full stack experience. It's fully unfinished, might not ever be finished, and might actually be a full waste of time, but it's gonna be a fun one and who knows, maybe it'll serve as a good framework for a real project.

## Features

- **User Authentication**: Securely sign up, log in, and manage your account to access personalized features.
- **Match Recording**: Record match details including players, teams, scores, duration, and key gameplay events.
- **Comprehensive Statistics**: Gain insights into your performance with detailed statistics including win/loss ratio, average score, most played maps, and more.
- **Leaderboards**: Compete with other players and climb the global leaderboards based on your performance.
- **Interactive Charts**: Visualize your progress and compare your stats over time with interactive charts.
- **Responsive Design**: Enjoy a seamless experience across devices, whether you're using a desktop, tablet, or smartphone.

## Technologies Used

- **Frontend**: React, TypeScript
- **Backend**: FastAPI, SQLAlchemy, GraphQL
- **Database**: SQL (SQLite, PostgreSQL, etc.)
- **Authentication**: TBD
- **Charting Library**: TBD
- **Deployment**: TBD

## Getting Started

1. Clone the repository: `git clone https://github.com/yourusername/war-of-wands-tracker.git`
2. Navigate to the project directory: `cd war-of-wands-tracker`
3. Install dependencies:
   - For the backend, navigate to the `backend` directory and run: `pip install -r requirements.txt`
   - For the frontend, navigate to the `frontend` directory and run: `npm install`
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Define the following variables:
     - For the backend:
       - `DATABASE_URL`: Database connection URL
       - `JWT_SECRET`: Secret key for JWT authentication
     - For the frontend:
       - `REACT_APP_API_URL`: Backend API URL
5. Start the backend server: 
   - Navigate to the `backend` directory and run: `uvicorn main:app --reload`
6. Start the frontend development server:
   - Navigate to the `frontend` directory and run: `npm start`
7. Access the application at `http://localhost:3000`

## Contributing

Contributions are welcome! If you have any ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the vibrant gaming community of "War of Wands"
- Special thanks to the developers of FastAPI, SQLAlchemy, React, TypeScript, and other open-source technologies that made this project possible.
