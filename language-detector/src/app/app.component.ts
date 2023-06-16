import { Component } from '@angular/core'
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  textInput: string = ''
  result: string = ''
  loading: boolean = false

  constructor(private http: HttpClient) { }

  detectLanguage() {
    this.loading = true

    this.http.get<any>(`http://localhost:5000/detect-language?input_text=${this.textInput}`)
      .subscribe({
        next: (response) => {
          this.result = `This text is in ${response.language_code}`
          this.loading = false
        },
        error: (error) => {
          console.error('Error occurred during language detection:', error)
          this.loading = false
        }
      })
  }

  enterKey(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      event.preventDefault()
      this.detectLanguage()
    }
  }
}