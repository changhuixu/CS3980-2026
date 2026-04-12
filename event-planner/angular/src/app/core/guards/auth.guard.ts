import { inject } from '@angular/core';
import { CanMatchFn, Route, Router, UrlSegment } from '@angular/router';
import { AuthService } from '../services/auth.service';

export const authGuard: CanMatchFn = (route: Route, _: UrlSegment[]) => {
  const router = inject(Router);
  const authService = inject(AuthService);

  const navigation = router.currentNavigation();
  const returnUrl = navigation?.extractedUrl.toString() || '/';
  const roles = ((route.data || {})['roles'] || []) as Array<string>;

  const role = authService.user().role;
  if (role) {
    if (!roles.includes(role)) {
      router.navigateByUrl('/access-denied');
      return false;
    }
    return true;
  } else {
    router.navigate(['login'], {
      queryParams: { returnUrl },
    });
    return false;
  }
};
