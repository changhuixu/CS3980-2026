import { HttpClient } from '@angular/common/http';
import { Component, inject, OnInit, signal } from '@angular/core';
import { UiowaRing } from '@uiowa/spinner';
import { finalize } from 'rxjs';
import { users_url } from '../../api-urls';
import { AuthService } from '../../core';
interface User {
  id: string;
  email: string;
  role: string;
  active: boolean;
}

@Component({
  selector: 'app-all-users',
  imports: [UiowaRing],
  templateUrl: './all-users.html',
  styleUrl: './all-users.css',
})
export class AllUsers implements OnInit {
  private readonly api = users_url;
  private http: HttpClient = inject(HttpClient);
  authSvc = inject(AuthService);
  username = this.authSvc.user().username;
  users = signal<User[]>([]);
  loading = signal(false);
  busy = signal(false);

  ngOnInit(): void {
    this.loading.set(true);
    this.http
      .get<User[]>(this.api)
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe((x) => {
        this.users.set(x);
        this.loading.set(false);
      });
  }

  updateStatus(user: User) {
    this.busy.set(true);
    this.http
      .put(`${this.api}/${user.id}/status`, {})
      .pipe(finalize(() => this.busy.set(false)))
      .subscribe((_) => {
        this.users.update((users) =>
          users.map((u) => (u.id === user.id ? { ...u, active: !user.active } : u)),
        );
      });
  }
}
