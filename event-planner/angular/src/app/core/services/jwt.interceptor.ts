import { HttpEvent, HttpHandlerFn, HttpRequest } from '@angular/common/http';
import { inject } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

export function jwtInterceptor(
  request: HttpRequest<unknown>,
  next: HttpHandlerFn,
): Observable<HttpEvent<unknown>> {
  const authService = inject(AuthService);
  const accessToken = authService.user().access_token;
  if (accessToken) {
    request = request.clone({
      setHeaders: { Authorization: `Bearer ${accessToken}` },
    });
  }

  return next(request);
}
