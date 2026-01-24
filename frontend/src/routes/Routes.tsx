import { Navigate, Route, Routes as RouterRoutes } from "react-router-dom";

import { DashboardPage } from "../modules/Dashboard/DashboardPage";
import { LandingPage } from "../modules/Landing/LandingPage";
import { LoginPage } from "../modules/Auth/LoginPage";
import { RegisterPage } from "../modules/Auth/RegisterPage";
import { OnboardingPage } from "../modules/Onboarding/OnboardingPage";
import { QuizPage } from "../modules/Quiz/QuizPage";
import { ResultsPage } from "../modules/Results/ResultsPage";
import { useAuthStore } from "../stores/authStore";

const ProtectedRoute = ({ children }: { children: JSX.Element }) => {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);
  return isAuthenticated ? children : <Navigate to="/login" replace />;
};

export const Routes = () => {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);

  return (
    <RouterRoutes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route
        path="/onboarding"
        element={
          <ProtectedRoute>
            <OnboardingPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <DashboardPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/quiz/:id"
        element={
          <ProtectedRoute>
            <QuizPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/results/:id"
        element={
          <ProtectedRoute>
            <ResultsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="*"
        element={<Navigate to={isAuthenticated ? "/dashboard" : "/"} replace />}
      />
    </RouterRoutes>
  );
};
