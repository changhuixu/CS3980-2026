import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { LoadingBar, UiowaRing } from '@uiowa/spinner';
import { finalize } from 'rxjs';
import { AuthService } from '../../core';
import { Event, EventsService } from '../events.service';

@Component({
  selector: 'app-all-events',
  imports: [RouterLink, UiowaRing, LoadingBar, FormsModule],
  templateUrl: './all-events.html',
  styleUrl: './all-events.css',
})
export class AllEvents {
  authSvc = inject(AuthService);
  username = this.authSvc.user().username;
  private readonly svc = inject(EventsService);
  private modalService = inject(NgbModal);
  events: Event[] = [];
  title = '';
  image = '';
  description = '';
  tags: string[] = [];
  location = '';
  busy = signal(false);
  loading = signal(false);

  private modalRef?: NgbModalRef;

  ngOnInit(): void {
    this.loading.set(true);
    this.svc
      .getAllEvents()
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe((x) => {
        this.events = x;
      });
  }

  open(content: any) {
    this.modalRef = this.modalService.open(content, {
      size: 'lg',
      ariaLabelledBy: 'modal-title',
      backdrop: 'static',
    });
  }

  removeTag(t: string) {
    this.tags = this.tags.filter((x) => x !== t);
  }
  addTag(t: string) {
    if (t && !this.tags.includes(t)) {
      this.tags.push(t);
    }
  }

  create(content: any) {
    this.busy.set(true);
    this.svc
      .createEvent(this.title, this.image, this.description, this.tags, this.location)
      .pipe(finalize(() => this.busy.set(false)))
      .subscribe((_) => {
        this.ngOnInit();
        this.modalRef?.close();
        this.open(content);
      });
  }

  delete(id: string) {
    this.svc.deleteEvent(id).subscribe((_) => {
      this.ngOnInit();
      this.modalRef?.close();
    });
  }
}
