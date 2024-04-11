import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AppModule } from './app.module';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  providers: [AppModule]
})

export class AppComponent {
  title = 'shopping-app-ui';
}
