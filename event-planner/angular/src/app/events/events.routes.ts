import { AllEvents } from './all-events/all-events';
import { EventDetails } from './event-details/event-details';

export const EventsRoutes = [
  { path: '', component: AllEvents },
  {
    path: ':guid',
    component: EventDetails,
  },
];
