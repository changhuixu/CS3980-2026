import { Routes } from '@angular/router';
import { authGuard } from './core';
import { Home } from './home/home';
import { Login } from './login/login';
import { SignUp } from './sign-up/sign-up';

export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    component: Home,
    canMatch: [authGuard],
    data: { roles: ['BasicUser', 'Admin', 'SuperAdmin'] },
  },
  { path: 'login', component: Login },
  { path: 'signup', component: SignUp },
  {
    path: 'events',
    loadChildren: () => import('./events/events.routes').then((m) => m.EventsRoutes),
    canMatch: [authGuard],
    data: { roles: ['BasicUser', 'Admin', 'SuperAdmin'] },
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes').then((m) => m.AdminRoutes),
    canMatch: [authGuard],
    data: { roles: ['SuperAdmin'] },
  },
  {
    path: 'access-denied',
    loadComponent: () => import('./access-denied/access-denied').then((m) => m.AccessDenied),
  },

  { path: '**', redirectTo: '' },
];
